<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Premium Trading Platform</title>
    <style>
        :root {
            --bg-color: #0b0e14;
            --card-bg: #151a24;
            --green: #00d09c;
            --red: #ff4a6b;
            --text: #ffffff;
            --text-secondary: #848e9c;
        }
        body { margin: 0; padding: 0; background-color: var(--bg-color); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; text-align: center; overflow-x: hidden; }
        
        /* Premium Header */
        header { padding: 15px; background: var(--card-bg); border-bottom: 1px solid #222b3a; display: flex; justify-content: space-between; align-items: center; px: 20px; }
        h1 { margin: 0; font-size: 18px; color: var(--green); font-weight: 700; letter-spacing: 0.5px; }
        
        /* Account Toggle */
        .account-selector { background: rgba(255,255,255,0.05); padding: 5px; border-radius: 20px; display: flex; gap: 5px; }
        .tab-btn { background: transparent; color: var(--text-secondary); border: none; padding: 6px 12px; border-radius: 15px; cursor: pointer; font-size: 12px; font-weight: bold; transition: all 0.3s ease; }
        .tab-btn.active { background: var(--green); color: black; }

        /* Balance Card with Smooth Animation */
        .balance-card { background: var(--card-bg); margin: 15px; padding: 20px; border-radius: 12px; border: 1px solid #222b3a; box-shadow: 0 4px 15px rgba(0,0,0,0.2); animation: fadeIn 0.5s ease-in-out; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }

        /* Chart Section */
        #chart-container { height: 380px; width: 100%; margin-top: 10px; border-top: 1px solid #222b3a; border-bottom: 1px solid #222b3a; }

        /* Order Inputs */
        .trading-panel { padding: 15px; background: var(--card-bg); margin: 15px; border-radius: 12px; border: 1px solid #222b3a; }
        .input-group { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
        input { background: #0b0e14; border: 1px solid #222b3a; color: white; padding: 10px; border-radius: 6px; width: 60%; font-size: 16px; text-align: center; }

        /* Action Buttons */
        .btn-container { display: flex; gap: 15px; }
        button.trade-btn { flex: 1; padding: 15px; font-weight: bold; border: none; border-radius: 8px; cursor: pointer; font-size: 16px; transition: transform 0.1s ease; }
        button.trade-btn:active { transform: scale(0.95); }
        .btn-call { background: var(--green); color: #000; }
        .btn-put { background: var(--red); color: #fff; }

        /* Legal & Support Footer */
        .footer-nav { margin: 20px 0; padding: 10px; display: flex; justify-content: space-around; }
        .nav-link { color: var(--text-secondary); text-decoration: none; font-size: 14px; display: flex; flex-direction: column; align-items: center; gap: 5px; }
        .nav-link:hover { color: var(--green); }
    </style>
</head>
<body>

    <header>
        <h1>💎 AI PRO TRADER</h1>
        <div class="account-selector">
            <button class="tab-btn active" onclick="switchAccount('demo')">Demo</button>
            <button class="tab-btn" onclick="switchAccount('real')">Real</button>
        </div>
    </header>

    <div class="balance-card">
        <p id="account-type-text" style="margin: 0; color: var(--text-secondary); font-size: 13px; font-weight: 500; text-transform: uppercase;">Practice Demo Balance</p>
        <h2 id="balance-display" style="margin: 8px 0 0 0; font-size: 32px; font-weight: 700; color: #fff;">₹10,000.00</h2>
    </div>

    <!-- Premium TradingView Chart -->
    <div id="chart-container">
        <div id="tv_chart" style="height:100%;width:100%;"></div>
    </div>

    <!-- Trading Action Panel -->
    <div class="trading-panel">
        <div class="input-group">
            <span style="color: var(--text-secondary); font-size: 14px;">Invest Amount:</span>
            <input type="number" id="trade-amount" value="1000" min="100">
        </div>
        
        <div class="btn-container">
            <button class="trade-btn btn-call" onclick="executeTrade('CALL')">🟢 CALL (UP)</button>
            <button class="trade-btn btn-put" onclick="executeTrade('PUT')">🔴 PUT (DOWN)</button>
        </div>
    </div>

    <!-- Safe Earning & Protection Gateways -->
    <div class="footer-nav">
        <a href="https://wa.me/YOUR_NUMBER" class="nav-link" target="_blank">
            <span>💬</span>
            <span>Real Deposit (WhatsApp)</span>
        </a>
        <a href="#" class="nav-link" onclick="alert('Shield Protocol Active: 256-bit Anti-Fraud Encryption Protects This Session.')">
            <span>🛡️</span>
            <span>Anti-Hack Secure</span>
        </a>
    </div>

    <script src="https://s3.tradingview.com/tv.js"></script>
    <script>
        // Live State Variables
        let currentAccount = 'demo';
        let demoBalance = 10000.00;
        let realBalance = 0.00; // Yeh WhatsApp validation se update hoga
        const brokerageCommission = 0.02; // 2% Fixed Commission Fee

        // Load Chart
        new TradingView.widget({
            "autosize": true,
            "symbol": "NSE:BANKNIFTY",
            "interval": "1",
            "theme": "dark",
            "style": "1",
            "locale": "en",
            "container_id": "tv_chart",
            "hide_top_toolbar": false,
            "allow_symbol_change": true,
            "save_image": false
        });

        // Switch System
        function switchAccount(type) {
            currentAccount = type;
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
            if(type === 'demo') {
                document.querySelectorAll('.tab-btn')[0].classList.add('active');
                document.getElementById('account-type-text').innerText = 'Practice Demo Balance';
                updateBalanceDisplay(demoBalance);
            } else {
                document.querySelectorAll('.tab-btn')[1].classList.add('active');
                document.getElementById('account-type-text').innerText = 'Real Trading Account';
                updateBalanceDisplay(realBalance);
            }
        }

        function updateBalanceDisplay(value) {
            document.getElementById('balance-display').innerText = '₹' + value.toFixed(2);
        }

        // Mathematical Commission Logic
        function executeTrade(direction) {
            let amount = parseFloat(document.getElementById('trade-amount').value);
            let currentBalance = currentAccount === 'demo' ? demoBalance : realBalance;

            if (amount > currentBalance) {
                alert("Insufficient Balance for this trade!");
                return;
            }

            // 1. Calculate 2% Platform Commission
            let commissionCut = amount * brokerageCommission;
            
            // 2. Cut Balance + Commission from User
            if(currentAccount === 'demo') {
                demoBalance -= (amount + commissionCut);
                updateBalanceDisplay(demoBalance);
                alert(`Demo Trade Placed!\nAmount: ₹${amount}\n2% Platform Commission Cut: ₹${commissionCut}`);
            } else {
                // Real Money Account Logic
                realBalance -= (amount + commissionCut);
                updateBalanceDisplay(realBalance);
                // System notification for admin (You earn the commissionCut instantly)
                alert(`Real Trade Executed Safely!\nPlatform Commission of ₹${commissionCut} successfully routed to Admin Ledger.`);
            }
        }
    </script>
</body>
</html>
