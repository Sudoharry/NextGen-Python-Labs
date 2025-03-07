class Calculator {
    constructor() {
        this.display = document.getElementById('display');
        this.currentInput = '0';
        this.initializeEventListeners();
    }

    initializeEventListeners() {
        document.querySelectorAll('.btn').forEach(button => {
            button.addEventListener('click', (e) => this.handleButtonPress(e.target));
        });
    }

    handleButtonPress(button) {
        const action = button.dataset.action;
        const operator = button.dataset.operator;
        const number = button.textContent;

        if (action) this.handleAction(action);
        if (operator) this.handleOperator(operator);
        if (number && !action && !operator) this.handleNumber(number);
    }

    handleAction(action) {
        switch(action) {
            case 'clear':
                this.currentInput = '0';
                break;
            case 'sign':
                this.currentInput = (-parseFloat(this.currentInput)).toString();
                break;
            case 'percent':
                this.currentInput = (parseFloat(this.currentInput)/100).toString();
                break;
            case 'calculate':
                this.calculateResult();
                break;
        }
        this.updateDisplay();
    }

    handleNumber(number) {
        if (this.currentInput === '0') {
            this.currentInput = number;
        } else {
            this.currentInput += number;
        }
        this.updateDisplay();
    }

    handleOperator(operator) {
        const lastChar = this.currentInput.slice(-1);
        const operators = ['+', '-', '×', '÷'];
        
        if (operators.includes(lastChar)) {
            this.currentInput = this.currentInput.slice(0, -1) + operator;
        } else {
            this.currentInput += operator;
        }
        this.updateDisplay();
    }

    async calculateResult() {
        try {
            const response = await fetch('/calculate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ expression: this.currentInput })
            });

            if (!response.ok) throw new Error('Calculation error');
            
            const data = await response.json();
            this.currentInput = data.result;
            this.updateDisplay();
        } catch (error) {
            this.currentInput = 'Error';
            this.updateDisplay();
            setTimeout(() => this.clearDisplay(), 1500);
        }
    }

    updateDisplay() {
        this.display.textContent = this.currentInput.slice(0, 12);
    }

    clearDisplay() {
        this.currentInput = '0';
        this.updateDisplay();
    }
}

// Initialize calculator when DOM loads
document.addEventListener('DOMContentLoaded', () => new Calculator());