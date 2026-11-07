# 📅 Quant Journey Daily Log

## 2026-11-07: Infrastructure Setup & First Strategy Implementation

### 🛠️ Technical Achievements
- **Environment Architecture**: Successfully established a professional quant stack: `Anaconda` $\rightarrow$ `Python 3.10` $\rightarrow$ `PyTorch (GPU)` $\rightarrow$ `VS Code` $\rightarrow$ `Jupyter Notebook`.
- **Workflow Automation**: Configured a Git-based synchronization pipeline with GitHub to ensure a transparent and version-controlled research process.
- **First Strategy**: Implemented a Moving Average (MA20) Crossover strategy for AAPL. The pipeline includes:
    - Data acquisition via `yfinance`.
    - Signal generation using vectorized Pandas operations.
    - Cumulative return backtesting with a benchmark comparison.

### 🧠 Key Insights & Reflections
**1. On Data Integrity:**
- Encountered `YFRateLimitError`. Learned that API rate limiting is a common challenge in quant research. 
- **Solution**: Implemented a "Mock Data Mode" to ensure logic validation remains uninterrupted during API outages.

**2. On Mathematical Rigor:**
- Encountered a `ValueError` regarding operand alignment in Pandas. 
- **Resolution**: Used `.values` to convert Series to NumPy arrays, effectively bypassing index alignment issues.
- **Look-ahead Bias**: Realized the critical importance of `.shift(1)` in backtesting. Without this, the strategy would use today's closing price to decide today's trade, which is an impossible "cheat" in real-world trading.

**3. On Professionalism:**
- Transitioned all code and documentation to professional English to align with global quant standards (e.g., Wall Street/Baruch MFE).
- Implemented a structured repository architecture to distinguish between `Mathematics`, `Coding`, and `Strategies`.

### 🚀 Next Steps
- [ ] Conduct a **Parameter Sweep** on the MA window (test 5, 10, 50, 200) to analyze strategy robustness.
- [ ] Explore **Max Drawdown** and **Sharpe Ratio** to evaluate risk-adjusted returns.
