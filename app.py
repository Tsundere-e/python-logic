import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(layout="wide", page_title="Strawberry Logic Studio")
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Strawberry Logic Studio | Web Edition</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;700&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    
    <style>
        /* Custom Font Application */
        body { font-family: 'Quicksand', sans-serif; }
        .font-mono { font-family: 'Fira Code', monospace; }

        /* Custom Scrollbar for Terminal */
        .custom-scroll::-webkit-scrollbar {
            width: 8px;
        }
        .custom-scroll::-webkit-scrollbar-track {
            background: rgba(45, 27, 36, 0.1);
        }
        .custom-scroll::-webkit-scrollbar-thumb {
            background: #ff69b4;
            border-radius: 4px;
        }

        /* Toggle Switch Styling */
        .toggle-checkbox:checked {
            right: 0;
            border-color: #ff69b4;
        }
        .toggle-checkbox:checked + .toggle-label {
            background-color: #ff69b4;
        }
        
        /* Slider Styling */
        input[type=range]::-webkit-slider-thumb {
            -webkit-appearance: none;
            height: 20px;
            width: 20px;
            border-radius: 50%;
            background: #ff69b4;
            cursor: pointer;
            margin-top: -8px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        }
        input[type=range]::-webkit-slider-runnable-track {
            width: 100%;
            height: 4px;
            cursor: pointer;
            background: #fecfef;
            border-radius: 2px;
        }

        /* Card Hover Effects */
        .logic-card {
            transition: all 0.3s ease;
        }
        .logic-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(255, 105, 180, 0.2);
        }

        /* Chart Container Specifics */
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
            height: 300px;
            max-height: 400px;
        }
    </style>

    <!-- Chosen Palette: Strawberry Cream (Warm Neutral Background #FFF0F5, Accents #FF69B4, #8B4367) -->
    <!-- Application Structure Plan: 
         1. Header: Branding and Session Context.
         2. Control Deck: Interactive Inputs (A, B, Voltage) & Terminal (Feedback Loop).
         3. Visualization Layer: Real-time Signal Chart (replacing static CSS wave) & Logic Matrix (Grid of results).
         4. Analytics: Tabular history of states.
         RATIONALE: This structure separates "Inputs" from "Outputs", flowing logically from top to bottom. The user changes a setting, sees the visual wave change, then reads the specific logic gate results.
    -->
    <!-- Visualization & Content Choices:
         1. Real-time Line Chart (Chart.js): Visualizes the "Pulse" (Voltage) over time. Goal: Show signal stability and magnitude.
         2. Logic Grid (HTML/CSS): 8 cards representing boolean gates. Goal: Instant read of logic states.
         3. Terminal (HTML/JS): Text-based log. Goal: Audit trail of user actions.
         4. History Table (HTML/JS): Data persistence. Goal: Detailed analysis.
    -->
    <!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->
</head>
<body class="bg-[#FFF0F5] text-[#8b4367] min-h-screen selection:bg-pink-200">

    <div class="container mx-auto px-4 py-8 max-w-7xl">
        
        <!-- HEADER SECTION -->
        <header class="mb-10 text-center animate-fade-in">
            <div class="inline-block bg-white border-2 border-pink-200 rounded-3xl px-8 py-6 shadow-lg shadow-pink-100/50">
                <div class="flex items-center justify-center gap-3 mb-2">
                    <span class="text-4xl filter drop-shadow-md">🍓</span>
                    <h1 class="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-[#ff69b4] to-[#8b4367]">
                        Strawberry Logic Studio
                    </h1>
                </div>
                <p class="text-pink-400 font-bold tracking-wider text-sm uppercase">Hardware Simulation Framework v4.1.0 • Web Edition</p>
            </div>
            
            <div class="mt-8 max-w-3xl mx-auto text-center">
                <p class="text-[#8b4367]/80 leading-relaxed">
                    Welcome to the <strong>Logic Studio Dashboard</strong>. This interactive application simulates digital logic gates and signal processing. 
                    Use the <strong>Bus Control</strong> to manipulate input signals (A/B) and voltage. Observe the real-time <strong>Signal Wave</strong> 
                    and analyze the resulting Boolean states in the <strong>Digital Matrix</strong> below.
                </p>
            </div>
        </header>

        <!-- MAIN CONTROL DECK -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 mb-8">
            
            <!-- INPUT CONTROLS -->
            <div class="lg:col-span-4 flex flex-col gap-6">
                <div class="bg-white rounded-3xl p-6 border border-pink-100 shadow-xl shadow-pink-100/40 h-full flex flex-col justify-center">
                    <h2 class="text-xl font-bold mb-6 flex items-center gap-2 border-b-2 border-pink-50 pb-2">
                        <span>🎛️</span> Bus Control
                    </h2>
                    
                    <!-- Toggle A -->
                    <div class="flex items-center justify-between mb-6 group">
                        <div class="flex flex-col">
                            <span class="font-bold text-lg">Bus Signal A</span>
                            <span class="text-xs text-pink-300 group-hover:text-pink-400 transition-colors">Input Stream 0x01</span>
                        </div>
                        <div class="relative inline-block w-14 mr-2 align-middle select-none transition duration-200 ease-in">
                            <input type="checkbox" name="toggle" id="toggleA" class="toggle-checkbox absolute block w-8 h-8 rounded-full bg-white border-4 border-pink-200 appearance-none cursor-pointer transition-all duration-300 ease-in-out top-0 left-0 hover:border-pink-300"/>
                            <label for="toggleA" class="toggle-label block overflow-hidden h-8 rounded-full bg-pink-100 cursor-pointer transition-colors duration-300"></label>
                        </div>
                    </div>

                    <!-- Toggle B -->
                    <div class="flex items-center justify-between mb-8 group">
                        <div class="flex flex-col">
                            <span class="font-bold text-lg">Bus Signal B</span>
                            <span class="text-xs text-pink-300 group-hover:text-pink-400 transition-colors">Input Stream 0x02</span>
                        </div>
                        <div class="relative inline-block w-14 mr-2 align-middle select-none transition duration-200 ease-in">
                            <input type="checkbox" name="toggle" id="toggleB" class="toggle-checkbox absolute block w-8 h-8 rounded-full bg-white border-4 border-pink-200 appearance-none cursor-pointer transition-all duration-300 ease-in-out top-0 left-0 hover:border-pink-300"/>
                            <label for="toggleB" class="toggle-label block overflow-hidden h-8 rounded-full bg-pink-100 cursor-pointer transition-colors duration-300"></label>
                        </div>
                    </div>

                    <!-- Voltage Slider -->
                    <div class="mb-2">
                        <div class="flex justify-between mb-2">
                            <label for="voltageSlider" class="font-bold">Core Voltage (V)</label>
                            <span id="voltageDisplay" class="font-mono text-[#ff69b4] font-bold bg-pink-50 px-2 rounded">3.3V</span>
                        </div>
                        <input type="range" min="1.2" max="5.0" step="0.1" value="3.3" id="voltageSlider" class="w-full h-2 bg-pink-100 rounded-lg appearance-none cursor-pointer">
                        <div class="flex justify-between text-xs text-pink-300 mt-1">
                            <span>1.2V</span>
                            <span>Logic Level</span>
                            <span>5.0V</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TERMINAL & STATUS -->
            <div class="lg:col-span-8">
                <div class="bg-[#2d1b24] text-pink-100 rounded-3xl p-6 shadow-xl shadow-pink-900/10 h-full flex flex-col border-l-8 border-[#ff69b4]">
                    <h2 class="text-lg font-bold mb-4 flex items-center gap-2 font-mono text-[#ff69b4]">
                        <span>>_</span> System Terminal
                    </h2>
                    <div id="terminal-output" class="font-mono text-sm overflow-y-auto flex-grow custom-scroll h-48 lg:h-auto space-y-2 p-2">
                        <div class="opacity-50">System Initialized...</div>
                        <div class="opacity-50">Loading Strawberry Kernel...</div>
                        <div class="text-[#ff69b4]">Ready. Waiting for input signal.</div>
                    </div>
                    <div class="mt-4 pt-3 border-t border-pink-900/50 flex justify-between items-center text-xs opacity-60 font-mono">
                        <span>STATUS: ACTIVE</span>
                        <span id="clock-display">00:00:00</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- VISUALIZATION LAYER -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 mb-12">
            
            <!-- WAVEFORM CHART -->
            <div class="lg:col-span-8 bg-white rounded-3xl p-6 border border-pink-100 shadow-xl shadow-pink-100/40">
                <div class="flex justify-between items-end mb-4">
                    <div>
                        <h2 class="text-xl font-bold text-[#8b4367]">🍓 Data Wave Monitor</h2>
                        <p class="text-sm text-pink-400">Real-time voltage output analysis</p>
                    </div>
                    <div class="flex gap-2 text-xs font-bold">
                        <span class="px-2 py-1 bg-pink-50 rounded text-pink-500">Live Feed</span>
                        <span class="px-2 py-1 bg-pink-50 rounded text-pink-500">100ms Polling</span>
                    </div>
                </div>
                
                <!-- Chart Container -->
                <div class="chart-container">
                    <canvas id="waveformChart"></canvas>
                </div>
                
                <div class="mt-4 flex justify-center gap-8 text-sm font-bold text-[#8b4367]">
                    <div class="flex items-center gap-2">
                        <span class="w-3 h-3 rounded-full bg-[#ff69b4]"></span> Output Signal
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="w-3 h-3 rounded-full bg-[#fecfef]"></span> Threshold
                    </div>
                </div>
            </div>

            <!-- QUICK STATS -->
            <div class="lg:col-span-4 flex flex-col gap-4">
                <div class="bg-gradient-to-br from-[#ff9a9e] to-[#fecfef] rounded-3xl p-6 text-white shadow-lg h-full flex flex-col justify-center items-center text-center relative overflow-hidden">
                    <div class="absolute top-0 left-0 w-full h-full opacity-10 pointer-events-none">
                        <div class="w-20 h-20 bg-white rounded-full absolute -top-10 -left-10"></div>
                        <div class="w-40 h-40 bg-white rounded-full absolute bottom-10 -right-10"></div>
                    </div>
                    
                    <span class="text-6xl mb-4 transform hover:scale-110 transition-transform cursor-default">🍓</span>
                    <h3 class="text-2xl font-bold mb-1">Signal Pulse</h3>
                    <div id="pulse-status" class="text-4xl font-black bg-white/20 px-6 py-2 rounded-xl backdrop-blur-sm mb-2">LOW</div>
                    <p class="text-sm opacity-90">Combined Logic Gate Intensity</p>
                </div>
            </div>
        </div>

        <!-- DIGITAL MATRIX (LOGIC GRID) -->
        <section class="mb-12">
            <div class="flex items-center justify-center gap-4 mb-8">
                <div class="h-px bg-pink-200 flex-grow max-w-xs"></div>
                <h2 class="text-2xl font-bold text-center text-[#8b4367]">⊹ ˖ Digital Matrix Results ♡⸝⸝</h2>
                <div class="h-px bg-pink-200 flex-grow max-w-xs"></div>
            </div>

            <p class="text-center text-pink-400 mb-8 max-w-2xl mx-auto">
                This matrix displays the computed Boolean outputs based on the current states of <strong>Input A</strong> and <strong>Input B</strong>. 
                Values are calculated instantly by the client-side Strawberry Engine.
            </p>

            <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                <!-- Gate Cards generated dynamically or static structure updated by JS -->
                <div class="logic-card bg-white p-6 rounded-[2rem] border-4 border-pink-100 text-center shadow-sm" id="card-AND">
                    <div class="text-xl font-bold text-[#8b4367] mb-2">AND</div>
                    <div class="gate-value text-4xl font-bold text-[#ff69b4]">0</div>
                </div>
                <div class="logic-card bg-white p-6 rounded-[2rem] border-4 border-pink-100 text-center shadow-sm" id="card-OR">
                    <div class="text-xl font-bold text-[#8b4367] mb-2">OR</div>
                    <div class="gate-value text-4xl font-bold text-[#ff69b4]">0</div>
                </div>
                <div class="logic-card bg-white p-6 rounded-[2rem] border-4 border-pink-100 text-center shadow-sm" id="card-XOR">
                    <div class="text-xl font-bold text-[#8b4367] mb-2">XOR</div>
                    <div class="gate-value text-4xl font-bold text-[#ff69b4]">0</div>
                </div>
                <div class="logic-card bg-white p-6 rounded-[2rem] border-4 border-pink-100 text-center shadow-sm" id="card-NAND">
                    <div class="text-xl font-bold text-[#8b4367] mb-2">NAND</div>
                    <div class="gate-value text-4xl font-bold text-[#ff69b4]">1</div>
                </div>
                <div class="logic-card bg-white p-6 rounded-[2rem] border-4 border-pink-100 text-center shadow-sm" id="card-NOR">
                    <div class="text-xl font-bold text-[#8b4367] mb-2">NOR</div>
                    <div class="gate-value text-4xl font-bold text-[#ff69b4]">1</div>
                </div>
                <div class="logic-card bg-white p-6 rounded-[2rem] border-4 border-pink-100 text-center shadow-sm" id="card-XNOR">
                    <div class="text-xl font-bold text-[#8b4367] mb-2">XNOR</div>
                    <div class="gate-value text-4xl font-bold text-[#ff69b4]">1</div>
                </div>
                <div class="logic-card bg-white p-6 rounded-[2rem] border-4 border-pink-100 text-center shadow-sm" id="card-NOTA">
                    <div class="text-xl font-bold text-[#8b4367] mb-2">NOT A</div>
                    <div class="gate-value text-4xl font-bold text-[#ff69b4]">1</div>
                </div>
                <div class="logic-card bg-white p-6 rounded-[2rem] border-4 border-pink-100 text-center shadow-sm" id="card-NOTB">
                    <div class="text-xl font-bold text-[#8b4367] mb-2">NOT B</div>
                    <div class="gate-value text-4xl font-bold text-[#ff69b4]">1</div>
                </div>
            </div>
        </section>

        <!-- DATA HISTORY SECTION -->
        <section class="bg-white rounded-3xl p-8 border border-pink-100 shadow-xl shadow-pink-100/30">
            <div class="flex justify-between items-center mb-6">
                <div>
                    <h2 class="text-xl font-bold text-[#8b4367] flex items-center gap-2">
                        📊 Logic History Log
                    </h2>
                    <p class="text-sm text-pink-400">Record of state changes and outputs</p>
                </div>
                <button onclick="clearHistory()" class="px-4 py-2 bg-pink-50 text-pink-500 rounded-xl text-sm font-bold hover:bg-pink-100 transition-colors">
                    Clear Log
                </button>
            </div>
            
            <div class="overflow-x-auto">
                <table class="w-full text-left border-collapse">
                    <thead>
                        <tr class="text-xs font-bold text-pink-400 uppercase tracking-wider border-b-2 border-pink-100">
                            <th class="p-3">Timestamp</th>
                            <th class="p-3">Bus A</th>
                            <th class="p-3">Bus B</th>
                            <th class="p-3">Voltage</th>
                            <th class="p-3">Primary Output (AND)</th>
                            <th class="p-3">Inverted (NAND)</th>
                        </tr>
                    </thead>
                    <tbody id="history-body" class="text-sm font-mono text-[#8b4367]">
                        <!-- JS injected rows -->
                    </tbody>
                </table>
                <div id="empty-state" class="text-center py-8 text-pink-300 italic">No activity recorded yet. Change inputs to generate data.</div>
            </div>
        </section>

        <footer class="text-center py-12 text-pink-300 text-sm font-medium">
            <p>st.mowkanel / python-logic • Professional Build • 2026</p>
            <p class="mt-2 text-xs">Generated Interactive Dashboard Prototype</p>
        </footer>

    </div>

    <!-- JAVASCRIPT LOGIC -->
    <script>
        // --- 1. CONFIGURATION & STATE ---
        const state = {
            a: 0,
            b: 0,
            voltage: 3.3,
            history: [],
            chartData: Array(20).fill(0) // Initial chart buffer
        };

        // --- 2. THE STRAWBERRY LOGIC ENGINE ---
        class StrawberryEngine {
            static compute(a, b) {
                const iA = a ? 1 : 0;
                const iB = b ? 1 : 0;
                return {
                    "AND": iA & iB,
                    "OR": iA | iB,
                    "XOR": iA ^ iB,
                    "NAND": Number(!(iA & iB)),
                    "NOR": Number(!(iA | iB)),
                    "XNOR": Number(iA === iB),
                    "NOTA": Number(!iA),
                    "NOTB": Number(!iB)
                };
            }
        }

        // --- 3. UI CONTROLLERS ---
        const ui = {
            toggleA: document.getElementById('toggleA'),
            toggleB: document.getElementById('toggleB'),
            sliderV: document.getElementById('voltageSlider'),
            voltageDisplay: document.getElementById('voltageDisplay'),
            terminal: document.getElementById('terminal-output'),
            clock: document.getElementById('clock-display'),
            pulseStatus: document.getElementById('pulse-status'),
            historyBody: document.getElementById('history-body'),
            emptyState: document.getElementById('empty-state'),
            
            cards: {
                "AND": document.getElementById('card-AND'),
                "OR": document.getElementById('card-OR'),
                "XOR": document.getElementById('card-XOR'),
                "NAND": document.getElementById('card-NAND'),
                "NOR": document.getElementById('card-NOR'),
                "XNOR": document.getElementById('card-XNOR'),
                "NOTA": document.getElementById('card-NOTA'),
                "NOTB": document.getElementById('card-NOTB'),
            }
        };

        // --- 4. CHART INITIALIZATION ---
        const ctx = document.getElementById('waveformChart').getContext('2d');
        const waveformChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: Array(20).fill(''),
                datasets: [{
                    label: 'Signal Intensity (V)',
                    data: state.chartData,
                    borderColor: '#ff69b4',
                    backgroundColor: 'rgba(255, 105, 180, 0.2)',
                    borderWidth: 3,
                    tension: 0.4, // Smooth curves for organic wave feel
                    fill: true,
                    pointRadius: 2,
                    pointHoverRadius: 5
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                animation: {
                    duration: 800,
                    easing: 'linear'
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 6,
                        grid: { color: '#fff0f5' },
                        ticks: { color: '#8b4367', font: { family: 'Fira Code' } }
                    },
                    x: {
                        display: false // Hide time axis for clean wave look
                    }
                },
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        backgroundColor: '#ffffff',
                        titleColor: '#8b4367',
                        bodyColor: '#ff69b4',
                        borderColor: '#ffb6c1',
                        borderWidth: 2,
                        callbacks: {
                            label: function(context) {
                                return `Voltage: ${context.parsed.y}V`;
                            }
                        }
                    }
                }
            }
        });

        // --- 5. CORE LOGIC FUNCTIONS ---
        function updateLogic() {
            // Update State
            state.a = ui.toggleA.checked;
            state.b = ui.toggleB.checked;
            state.voltage = parseFloat(ui.sliderV.value);
            
            // Update UI Labels
            ui.voltageDisplay.innerText = state.voltage.toFixed(1) + "V";

            // Compute Logic
            const results = StrawberryEngine.compute(state.a, state.b);
            
            // Update Matrix Cards
            Object.keys(results).forEach(key => {
                const card = ui.cards[key];
                const valueDiv = card.querySelector('.gate-value');
                const val = results[key];
                
                valueDiv.innerText = val;
                
                // Visual feedback for High/Low
                if(val === 1) {
                    card.style.borderColor = '#ff69b4';
                    valueDiv.style.textShadow = '0 0 10px rgba(255,105,180,0.5)';
                } else {
                    card.style.borderColor = '#fff0f5'; // Light pink border
                    valueDiv.style.textShadow = 'none';
                }
            });

            // Update Pulse Status text
            const isHigh = state.a || state.b;
            ui.pulseStatus.innerText = isHigh ? "HIGH" : "LOW";
            ui.pulseStatus.style.color = isHigh ? "#ff69b4" : "#8b4367";

            // Log to Terminal
            logToTerminal(`Input Change detected: A=${Number(state.a)} B=${Number(state.b)} V=${state.voltage}`);
            
            // Add to History
            addToHistory(results);
            
            // Update Chart Data (Immediate spike visual)
            updateChart();
        }

        function updateChart() {
            // Logic for visual wave: If A or B is on, signal = voltage. Else ~0.2 (noise)
            const noise = (Math.random() * 0.2);
            const signalLevel = (state.a || state.b) ? state.voltage : 0.2 + noise;
            
            // Shift array
            state.chartData.shift();
            state.chartData.push(signalLevel);
            
            waveformChart.data.datasets[0].data = state.chartData;
            waveformChart.update('none'); // 'none' mode for performance
        }

        // --- 6. UTILITY FUNCTIONS ---
        function logToTerminal(msg) {
            const time = new Date().toLocaleTimeString();
            const line = document.createElement('div');
            line.innerHTML = `<span class="opacity-50">[${time}]</span> ${msg}`;
            ui.terminal.appendChild(line);
            ui.terminal.scrollTop = ui.terminal.scrollHeight;
        }

        function addToHistory(results) {
            const time = new Date().toLocaleTimeString();
            const row = document.createElement('tr');
            row.className = "border-b border-pink-50 hover:bg-pink-50/50 transition-colors";
            
            row.innerHTML = `
                <td class="p-3 opacity-70">${time}</td>
                <td class="p-3 font-bold ${state.a ? 'text-pink-500' : 'text-gray-400'}">${state.a ? '1' : '0'}</td>
                <td class="p-3 font-bold ${state.b ? 'text-pink-500' : 'text-gray-400'}">${state.b ? '1' : '0'}</td>
                <td class="p-3">${state.voltage}V</td>
                <td class="p-3">${results['AND']}</td>
                <td class="p-3">${results['NAND']}</td>
            `;
            
            // Insert at top
            ui.historyBody.insertBefore(row, ui.historyBody.firstChild);
            
            // Limit history rows
            if(ui.historyBody.children.length > 10) {
                ui.historyBody.removeChild(ui.historyBody.lastChild);
            }

            ui.emptyState.style.display = 'none';
        }

        function clearHistory() {
            ui.historyBody.innerHTML = '';
            ui.emptyState.style.display = 'block';
            logToTerminal("System Log Cleared.");
        }

        function updateClock() {
            ui.clock.innerText = new Date().toLocaleTimeString();
        }

        // --- 7. EVENT LISTENERS ---
        ui.toggleA.addEventListener('change', updateLogic);
        ui.toggleB.addEventListener('change', updateLogic);
        ui.sliderV.addEventListener('input', () => {
            ui.voltageDisplay.innerText = parseFloat(ui.sliderV.value).toFixed(1) + "V";
        });
        ui.sliderV.addEventListener('change', updateLogic); // Trigger logic update on release

        // Animation Loop for living chart (Heartbeat effect)
        setInterval(() => {
            // Even if inputs don't change, we want the chart to scroll slightly or show noise
            updateChart();
        }, 800);

        setInterval(updateClock, 1000);

        // --- 8. INITIALIZATION ---
        window.onload = () => {
            logToTerminal("Hardware Connection Established.");
            updateLogic();
        };

    </script>
</body>
</html>
"""
components.html(html_code, height=1200, scrolling=True)

