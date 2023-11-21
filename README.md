# Django Warehouse Management System (WMS)

Welcome to the Django Warehouse Management System! This system is designed to help manage and streamline warehouse operations, including inventory tracking, order fulfillment, and more.

## Getting Started

### Prerequisites

Before running the WMS, make sure you have the following installed on your system:

- Python (3.10.12)
- Django
- PostgreSQL (or another database supported by Django)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/charles-okunzo/Warehouse-Management-System.git
    ```

2. Change into the project directory:

    ```bash
    cd Warehouse-Management-System
    ```
3. Create your environment:

    ```bash
    pip install virtualenv
    virtualenv myenv
    source myenv/bin/activate
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Create and apply migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Create a superuser for admin access:

    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

The WMS should now be running at `http://localhost:8000/`. Access the admin interface at `http://localhost:8000/admin/` using the superuser credentials created earlier.

## Features

- **User Authentication:** Secure user authentication and authorization.
- **Product Management:** Add, edit, and delete products with detailed information.
- **Inventory Tracking:** Keep track of inventory levels and monitor stock movements.
- **Order Management:** Manage customer orders, process shipments, and track order status.
- **Reports:** Generate reports on inventory, sales, and other relevant metrics.
- **User Roles:** Assign roles to users for granular access control.

## Configuration

- **Database:** Configure your preferred database settings in `settings.py`.
- **Environment Variables:** Set environment variables for sensitive information like secret keys, database credentials, etc.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Thank you to the Django community for providing an excellent web framework.
- Special thanks to [contributors](CONTRIBUTORS.md) who have helped improve this project.

