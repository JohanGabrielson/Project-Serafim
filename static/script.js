async function loadSystemStatus() {
    try {
        //const res = await fetch("/api/system");
        const res = await fetch("/api/system");
        const data = await res.json();
        console.log("DATA FROM API:", data);


        //UI-elements
        document.getElementById("uptime").textContent = data.uptime;
        document.getElementById("version").textContent = `${data.version} (${data.commit})`;
        document.getElementById("serverTime").textContent = data.server_time;

    
        //document.getElementById("os").textContent = data.os;
        //document.getElementById("kernel").textContent = data.kernel;
        //document.getElementById("load").textContent = data.load.join(" / ");

        document.getElementById("os").textContent = data.system + " " + data.release;
        document.getElementById("kernel").textContent = data.release;
        document.getElementById("load").textContent = data.load.join(" / ");
    } catch (error) {
        console.error("Failed to load system status:", error);
    }
}

// Update every 3 seconds
setInterval(loadSystemStatus, 3000);
loadSystemStatus();

// metrics
async function loadMetrics() {
    try {
        const cpu = await fetch('/api/metrics/cpu').then(r => r.json());
        const ram = await fetch('/api/metrics/ram').then(r => r.json());
        const disk = await fetch('/api/metrics/disk').then(r => r.json());

        document.getElementById('cpu').textContent = cpu.cpu_percent + "%";
        document.getElementById('ram').textContent = ram.percent + "%";
        document.getElementById('disk').textContent = disk.percent + "%";

    } catch (err) {
        console.error("Metrics error:", err);
    }
}

setInterval(loadMetrics, 2000);
loadMetrics();

document.getElementById("toggle-extra").addEventListener("click", () => {
    const box = document.getElementById("system-extra");
    const btn = document.getElementById("toggle-extra");

    if (box.style.display === "none") {
        box.style.display = "block";
        btn.textContent = "Show less";
    } else {
        box.style.display = "none";
        btn.textContent = "Show more";
    }
});

async function fetchLogs() {
    const container = document.getElementById("logs-container");

    // Är användaren längst ner?
    const isAtBottom =
        Math.abs(container.scrollHeight - container.scrollTop - container.clientHeight) < 5;

    try {
        const response = await fetch("/api/logs/");
        const data = await response.json();

        if (!data.logs || data.logs.length === 0) {
            container.textContent = "No logs available.";
            return;
        }

        // Bygg hela texten i en sträng (snabbt och stabilt)
        const fullText = data.logs.join("\n");

        // Uppdatera utan att nollställa scrollpositionen
        container.textContent = fullText;

        // Auto-scroll endast om användaren var längst ner
        if (isAtBottom) {
            container.scrollTop = container.scrollHeight;
        }

    } catch (err) {
        console.error("Error fetching logs:", err);
        container.textContent = "Failed to load logs.";
    }
}
fetchLogs();
setInterval(fetchLogs, 10000);

document.getElementById("restartBtn").addEventListener("click", () => {
    if (confirm("⚠️ WARNING! System Restart 🔄\n\nThis will restart the Serafim system. ")) {
        fetch("/api/restart", { method: "POST" });
    }
});

document.getElementById("shutdownBtn").addEventListener("click", () => {
    if (confirm("⚠️ WARNING! System Shutdown 🛑\n\nThis will shutdown the Serafim system.")) {
        fetch("/api/shutdown", { method: "POST" });
    }
});