<h1>Bus Booking System Backend</h1>
<h2>Overview</h2>
<p>The Bus Booking System is a web-based application that allows users to book bus tickets online, view bus schedules, select seats, make payments, and track buses in real time.</p> <p>This README provides information about the backend implementation of the system, including setup instructions, API details, and other essential information.</p>

<h2>Features</h2>
<ul>
<li><strong>User Registration & Authentication:</strong> Secure user registration, login, and logout.</li>
<li><strong>Profile Management:</strong> Users can manage their profiles, including updating contact information and payment methods.</li>
<li><strong>Bus Schedule Viewing:</strong> Users can view bus schedules and available routes.</li>
<li><strong>Interactive Seat Selection:</strong> Users can select seats on a bus, with availability status indicated.</li>
<li><strong>Booking & Payment:</strong> Secure booking process with payment integration (e.g., MPESA).</li>
<li><strong>QR Code Generation:</strong> Generate QR codes for tickets containing booking details.</li>
<li><strong>Real-Time Bus Tracking:</strong> Track buses in real time with a simulated tracking feature.</li>
<li><strong>Role-Based Access Control (RBAC):</strong> Different roles (e.g., student, parent, bus manager, admin) with specific permissions.</li>
<li><strong>Admin Dashboard:</strong> Manage buses, routes, bookings, and users with insights and statistics.</li>
</ul>
<h2>Tech Stack</h2>
<ul>
<li><strong>Backend Framework:</strong> Django</li>
<li><strong>API:</strong> Django REST Framework (DRF)</li>
<li><strong>Database:</strong> MySQL</li>
<li><strong>Authentication:</strong> Django Knox Tokens</li>
<li><strong>Payment Integration:</strong> MPESA</li>
<li><strong>SMS Integration:</strong> Twilio</li>
<li><strong>QR Code Generation:</strong> qrcode library</li>
</ul>
<h2>Installation</h2>
<h3>Prerequisites</h3>
<p>Python 3.8+</p>
<p>MySQL Database</p>
<p>Virtualenv (optional but recommended)</p>
<h3>Setup Instructions</h3>
<ol className='list:disc'>

<li><strong>Clone the Repository:</strong></li>

```
Copy code
git clone https://github.com/yourusername/bus-booking-system-backend.git
cd bus-booking-system-backend
```
<li><strong>Create and Activate a Virtual Environment:</strong></li>

```
Copy code
python3 -m venv venv
source venv/bin/activate
```
<li><strong>Install Dependencies:</strong></li>

```
Copy code
pip install -r requirements.txt
```
<li><strong>Set Up Environment Variables:</strong></li>

<p>Create a .env file in the project root and add the following:</p>

```
env

Copy code
SECRET_KEY=your_secret_key
DATABASE_NAME=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=localhost
DATABASE_PORT=3306

MPESA Credentials
MPESA_CONSUMER_KEY=your_mpesa_consumer_key
MPESA_CONSUMER_SECRET=your_mpesa_consumer_secret

 Twilio Credentials
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
```
<li><strong>Run Database Migrations:</strong></li>

```
Copy code
python manage.py migrate
```
<li><strong>Create a Superuser:</strong></li>

```
Copy code
python manage.py createsuperuser
```
<li><strong>Start the Development Server:</strong></li>

```
Copy Code
python manage.py runserver
```
</ol>
<h2>API Endpoints</h2>
<h3>Authentication</h3>
<ul>
<li><strong>Login:</strong> /api/auth/login/</li>
<li><strong>Logout:</strong> /api/auth/logout/</li>
<li><strong>Register:</strong> /api/auth/register/</li>
<li><strong>Password Reset:</strong> /api/auth/password-reset/</li>
</ul>
<h3>Profile Management</h3>
<ul>
<li><strong>Get Profile:</strong> /api/profile/</li>
<li><strong>Update Profile:</strong> /api/profile/update/</li>
</ul>
<h3>Bus and Route Management</h3>
<ul>
<li><strong>Get All Buses:</strong> /api/buses/</li>
<li><strong>Get Bus Details:</strong> /api/buses/{bus_id}/</li>
<li><strong>Get All Routes:</strong> /api/routes/</li>
<li><strong>Get Route Details:</strong> /api/routes/{route_id}/</li>
</ul>
<h3>Booking Management</h3>
<ul>
<li><strong>Book a Seat:</strong> /api/bookings/</li>
<li><strong>Get Booking Details:</strong> /api/bookings/{booking_id}/</li>
<li><strong>Cancel Booking:</strong> /api/bookings/{booking_id}/cancel/</li>
</ul>
<h3>Admin</h3>
<ul>
<li><strong>Dashboard:</strong> /api/admin/dashboard/</li>
<li><strong>Manage Buses:</strong> /api/admin/buses/</li>
<li><strong>Manage Routes:</strong> /api/admin/routes/</li>
<li><strong>Manage Bookings:</strong> /api/admin/bookings/</li>
</ul>
<h2>Running Tests</h2>
<p>To run tests, use the following command:</p>

```
Copy code
python manage.py test
```
<h2>Deployment</h2>
<p>For deployment, ensure that you have configured the necessary environment variables in your production environment.
Use tools like gunicorn and nginx for serving the Django application.</p>

<h2>Contributing</h2>
<p>Contributions are welcome! Please create a pull request or submit an issue if you have any suggestions or improvements.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the LICENSE file for details.</p>

<h2>Contact</h2>
<p>For any inquiries or support, please contact Tiffany Kanyingi at [kanyingitiffany@gmail.com].</p>