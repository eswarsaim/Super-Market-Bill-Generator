🛒 Super Market Bill Generator

A simple Python program that simulates a **billing system for a supermarket**.
This project allows customers to view available items, purchase products, and generates a final bill with **GST (Goods & Services Tax)** included.

📌 Features

* Displays a list of items available in the supermarket along with their prices.
* Allows customers to:

  * Select items to purchase
  * Enter quantity for each item
* Automatically calculates:

  * Price for each product
  * Total bill amount
  * GST (5%)
  * Final payable amount
* Generates a **well-structured bill receipt** with customer name and date-time.

---

🛠️ Technologies Used

* **Python 3**
* Built-in libraries:

  * `datetime` (for bill timestamp)

📂 Project Structure

```
supermarket-bill-generator/
│
├── bill_generator.py     # Main Python script
└── README.md             # Project documentation
```

🚀 How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/supermarket-bill-generator.git
   cd supermarket-bill-generator
   ```

2. Run the Python script:

   ```bash
   python bill_generator.py
   ```

3. Follow the instructions on the screen to generate your bill.

📸 Sample Output

```
========================= ESS Supermarket =========================
                            Pulivendula
Name: John Doe                          Date: 2025-08-16 20:15:34.123456
---------------------------------------------------------------------
s.no         Items          Quantity          Price
1            Rice           2                 40
2            Tea            1                 50
3            Biscuits       3                 30
---------------------------------------------------------------------
                                    Total Price:  Rs 120
                                    GST:          Rs 6.0
---------------------------------------------------------------------
                                    Final Amount: Rs 126.0
---------------------------------------------------------------------
                      Thank You Visit Again                      
---------------------------------------------------------------------

---


📈 Future Improvements

* Add more items dynamically from a file or database.
* Apply discount offers or promo codes.
* Export the bill as a **PDF or text file**.
* Add user authentication (admin/customer mode).

🤝 Contributing

Contributions are welcome! If you’d like to enhance this project:

1. Fork the repo
2. Create a new branch (`feature-xyz`)
3. Commit your changes
4. Submit a pull request

---

📜 License

This project is licensed under the **MIT License** – feel free to use and modify it.
