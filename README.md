# PyCoffeeMachine ☕

A simple Python Coffee Machine simulator that lets you select drinks, processes coins, checks resource availability, and makes coffee — all in the terminal.

---

## 📌 Features
- **Drink Selection**: Choose from espresso, latte, or cappuccino.
- **Resource Management**: Tracks available water, milk, coffee, and profit.
- **Coin Processing**: Accepts quarters, dimes, nickels, and pennies.
- **Transaction Handling**: Checks for sufficient funds, refunds if not enough, and gives change when needed.
- **Maintenance Commands**:
  - `report` → Prints current resources & profit.
  - `off` → Turns off the machine.

---

## 📂 Project Structure
```
PyCoffeeMachine/
│── cmmain.py # Main program logic
│── data.py # Drink menu, resources, and ASCII art
```


---

## ▶️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/ayovz/PyCoffeeMachine/
   ```
2. Navigate to the folder:
   ```
   cd PyCoffeeMachine
   ```
3. Run the program:
   ```
   python cmmain.py
   ```

# 🛠 Example Usage
```bash
 ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||C |||o |||f |||f |||e |||e |||       |||M |||a |||c |||h |||i |||n |||e ||
||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|

What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $0.0 in change.
Here's your Latte! Enjoy☕!

```

# 📜 License
If you want, I can also make you a **sample `LICENSE` file** so you can push this as a fully ready GitHub repo. That way your project will look polished and professional.  
Do you want me to prepare that?
