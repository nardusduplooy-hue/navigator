// --- Clock ---

function updateClock() {
  const now = new Date();
  const time = now.toLocaleTimeString('en-ZA', {
    timeZone: 'Africa/Johannesburg',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: false,
  });
  document.getElementById('clock').textContent = time + ' CAT';
}

setInterval(updateClock, 1000);
updateClock();

// --- Hero date ---

const DAYS = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY'];
const MONTHS = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER'];

const now = new Date();
document.getElementById('hero-date').textContent =
  DAYS[now.getDay()] + ' · ' +
  String(now.getDate()).padStart(2, '0') + ' ' +
  MONTHS[now.getMonth()] + ' ' +
  now.getFullYear();

// --- Countdowns ---

function getCountdown(target) {
  const diff = target - new Date();
  if (diff < 0) return 'OVERDUE';
  const d = Math.floor(diff / 86400000);
  const h = Math.floor((diff % 86400000) / 3600000);
  const m = Math.floor((diff % 3600000) / 60000);
  if (d > 0) return 'T−' + d + 'd ' + h + 'h';
  if (h > 0) return 'T−' + h + 'h ' + m + 'm';
  return 'T−' + m + 'm';
}

function updateCountdowns() {
  document.getElementById('cd-essay').textContent   = getCountdown(new Date('2026-03-23T17:00:00Z'));
  document.getElementById('cd-session').textContent  = getCountdown(new Date('2026-03-21T08:00:00Z'));
  document.getElementById('cd-module2').textContent  = getCountdown(new Date('2026-03-21T08:00:00Z'));
}

setInterval(updateCountdowns, 60000);
updateCountdowns();

// --- Calendar ---

let calYear = 2026;
let calMonth = 2;

const calEvents = {
  '2026-3-21': 'session-day',
  '2026-3-23': 'deadline',
};

function renderCalendar() {
  document.getElementById('cal-month-label').textContent = MONTHS[calMonth] + ' ' + calYear;

  const grid = document.getElementById('cal-grid');
  grid.innerHTML = '';

  ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'].forEach(d => {
    const el = document.createElement('div');
    el.className = 'cal-day-label';
    el.textContent = d;
    grid.appendChild(el);
  });

  const firstDay = new Date(calYear, calMonth, 1).getDay();
  const offset = firstDay === 0 ? 6 : firstDay - 1;
  const daysInMonth = new Date(calYear, calMonth + 1, 0).getDate();

  for (let i = 0; i < offset; i++) {
    const el = document.createElement('div');
    el.className = 'cal-day empty';
    grid.appendChild(el);
  }

  const today = new Date();

  for (let d = 1; d <= daysInMonth; d++) {
    const el = document.createElement('div');
    el.className = 'cal-day';
    el.textContent = d;

    const isToday =
      today.getFullYear() === calYear &&
      today.getMonth() === calMonth &&
      today.getDate() === d;

    if (isToday) el.classList.add('today');

    const key = calYear + '-' + (calMonth + 1) + '-' + d;
    if (calEvents[key]) {
      el.classList.add('has-event');
      el.classList.add(calEvents[key]);
    }

    grid.appendChild(el);
  }
}

function prevMonth() {
  calMonth--;
  if (calMonth < 0) { calMonth = 11; calYear--; }
  renderCalendar();
}

function nextMonth() {
  calMonth++;
  if (calMonth > 11) { calMonth = 0; calYear++; }
  renderCalendar();
}

renderCalendar();

// --- JTBD check toggle ---

function toggleCheck(el) {
  if (el.classList.contains('done')) {
    el.classList.remove('done');
    el.classList.add('in-progress');
  } else if (el.classList.contains('in-progress')) {
    el.classList.remove('in-progress');
  } else {
    el.classList.add('done');
  }
}

// --- API data ---

async function loadData() {
  const liveLabel = document.getElementById('live-label');
  liveLabel.textContent = 'SYNCING...';
  try {
    const res = await fetch('/api/data');
    if (!res.ok) throw new Error('offline');
    const data = await res.json();
    renderStats(data.stats);
    renderDeadlines(data.deadlines, data.sessions);
    renderImportantFeed(data.important);
    renderChannels(data.channels);
    document.getElementById('last-updated').textContent = data.stats.last_updated;
    liveLabel.textContent = 'LIVE';
  } catch (e) {
    liveLabel.textContent = 'OFFLINE';
    renderOfflineState();
  }
}

function renderStats(s) {
  document.getElementById('stat-messages').textContent  = s.total_messages;
  document.getElementById('stat-channels').textContent  = s.total_channels;
  document.getElementById('stat-important').textContent = s.total_important;
}

function renderDeadlines(deadlines, sessions) {
  const el = document.getElementById('deadlines-feed');

  let html = `
    <div class="deadline-item">
      <div class="deadline-name">Future of Work Essay</div>
      <div class="deadline-meta">📅 23 March 2026 · 19:00 CET</div>
      <span class="badge red">${getCountdown(new Date('2026-03-23T17:00:00Z'))}</span>
    </div>`;

  sessions.slice(0, 3).forEach(s => {
    const text = s.text.substring(0, 80) + (s.text.length > 80 ? '…' : '');
    html += `
    <div class="deadline-item session">
      <div class="deadline-name">${text}</div>
      <div class="deadline-meta">[${s.topic}] ${s.date}</div>
      <span class="badge green">SESSION</span>
    </div>`;
  });

  deadlines.slice(0, 3).forEach(d => {
    const text = d.text.substring(0, 80) + (d.text.length > 80 ? '…' : '');
    html += `
    <div class="deadline-item info">
      <div class="deadline-name">${text}</div>
      <div class="deadline-meta">[${d.topic}] ${d.date}</div>
      <span class="badge blue">DEADLINE REF</span>
    </div>`;
  });

  el.innerHTML = html;
}

function renderImportantFeed(items) {
  const el = document.getElementById('important-feed');
  const shown = items.filter(m => m.flagged).slice(0, 6);

  if (!shown.length) {
    el.innerHTML = '<div class="loading">NO FLAGGED MESSAGES</div>';
    return;
  }

  el.innerHTML = shown.map(m => {
    const text = m.text.substring(0, 120) + (m.text.length > 120 ? '…' : '');
    const tags = m.tags.length
      ? '<div class="feed-tags">' + m.tags.map(t => `<span class="badge blue">${t}</span>`).join('') + '</div>'
      : '';
    return `
    <div class="feed-item">
      <div class="feed-topic">${m.topic}</div>
      <div class="feed-text">${text}</div>
      <div class="feed-date">${m.date}</div>
      ${tags}
    </div>`;
  }).join('');
}

function renderChannels(channels) {
  const el = document.getElementById('channels-list');
  const sorted = channels.sort((a, b) => b.important - a.important);
  el.innerHTML = sorted.map(c => `
    <div class="channel-item">
      <span class="channel-name">${c.name}</span>
      <span class="channel-counts"><span>${c.important}</span> flagged · ${c.total} msgs</span>
    </div>`).join('');
}

function renderOfflineState() {
  document.getElementById('deadlines-feed').innerHTML = `
    <div style="font-family:var(--mono);font-size:10px;color:var(--text-dim);line-height:1.8;">
      Run <span style="color:var(--accent)">python server/server.py</span><br>to connect live data.
    </div>`;
  document.getElementById('important-feed').innerHTML = '';
  document.getElementById('channels-list').innerHTML = '<div class="loading">SERVER OFFLINE</div>';
  document.getElementById('stat-messages').textContent  = '—';
  document.getElementById('stat-channels').textContent  = '—';
  document.getElementById('stat-important').textContent = '—';
}

loadData();
setInterval(loadData, 300000);
