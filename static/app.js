* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: linear-gradient(135deg, #0f172a, #111827);
  color: #e5e7eb;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px;
}

.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
}

.eyebrow {
  margin: 0;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #7dd3fc;
  font-size: 12px;
}

h1, h2 {
  margin: 0;
}

.actions {
  display: flex;
  gap: 12px;
  align-items: center;
}

button, input {
  border-radius: 10px;
  border: 1px solid #334155;
  padding: 10px 14px;
  font-size: 14px;
}

button {
  background: #2563eb;
  color: white;
  cursor: pointer;
}

button:hover {
  background: #1d4ed8;
}

input {
  background: #0f172a;
  color: #e2e8f0;
  min-width: 220px;
}

.summary-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-bottom: 24px;
}

.card {
  background: rgba(15, 23, 42, 0.9);
  border: 1px solid #334155;
  border-radius: 16px;
  padding: 20px;
}

.stat-card {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.stat-card strong {
  font-size: 28px;
}

.content-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.item-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 16px;
}

.item {
  padding: 12px 14px;
  border-radius: 10px;
  background: #111827;
  border: 1px solid #334155;
}

.item small {
  display: block;
  color: #93c5fd;
  margin-top: 6px;
}

@media (max-width: 760px) {
  .topbar,
  .content-grid,
  .summary-grid {
    grid-template-columns: 1fr;
    display: grid;
  }

  .actions {
    flex-direction: column;
    align-items: stretch;
  }
}
