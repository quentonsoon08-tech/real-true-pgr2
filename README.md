# 📦 Stationery Inventory Management System

A Python command-line application for managing a stationery inventory. Built for **Module: Programming 2 (SF43002FP)**.

---

## 📋 Description

This program provides an interactive menu for managing stationery inventory. Users can add, edit, update sold items, display all items, and save the inventory to a CSV file.

---

## 📁 Files

| File | Description |
|------|-------------|
| `main.py` | Main script — runs the interactive menu and all inventory operations |
| `stationery.py` | Contains the `StationeryItem` class used to calculate total prices |

---

## ▶️ How to Run

Make sure you have Python 3 installed, then run:

```bash
python main.py
```

---

## 🗂️ Menu Options

| Option | Description |
|--------|-------------|
| 1 | Add a new stationery item |
| 2 | Edit an existing stationery item |
| 3 | Update stock after a sale |
| 4 | Display all stationery items |
| 5 | Save inventory to a `.csv` file |

---

## 🗃️ Sample Inventory (Pre-loaded)

| Name | Quantity | Price ($) |
|------|----------|-----------|
| Pen | 200 | 1.20 |
| Pencil | 250 | 0.80 |
| Eraser | 150 | 0.50 |
| Glue Stick | 100 | 1.10 |
| Writing Book | 300 | 1.50 |

---

## 💾 CSV Output

Selecting option **5** saves the inventory to:

```
stationery_inventory.csv
```

The file includes columns: `No., Name, Quantity, Price ($), Total Price ($)`

---

## 🧠 Concepts Used

- **Data types:** `str`, `int`, `float`
- **Keywords:** `while True`, `if`, `elif`, `else`, `for`, `break`, `continue`, `def`, `class`
- **OOP:** `StationeryItem` class with `calculate_total()` method
- **File I/O:** Writing inventory data to a CSV file
- **Input validation:** All user inputs are validated before being accepted

---

## ⚙️ Requirements

- Python 3.x
- No external libraries required (uses built-in `os` and `csv` modules)
