# Body Therapy

Live Version: [Body Therapy](https://body-therapy-proj5.onrender.com)

Repository: [GitHub Repo](https://github.com/Inna-Kot/body_therapy_proj5)

The app is developed by [Inna Kot](https://github.com/Inna-Kot).

## About

[Body Therapy](https://body-therapy-proj5.onrender.com) is a professional sports massage and injury recovery application designed for a private practice. The main goal of this app is to help clients easily discover therapy services, manage their bookings, and learn about injury prevention. Moreover, the app is aimed at increasing the efficiency of the therapist's schedule management and providing a seamless digital experience for the private practice members.

---

## User Experience Design (UX)

### Strategy & Target Audience
Developed for a professional private sports massage practice, the app focuses on intuitive navigation and clear call-to-action paths for booking sessions.
* **Site Owner (admin - Private Therapist):** Needs to manage service offerings, track bookings, and build trust through client reviews.
* **Returning Clients (Athletes/Patients):** Need a quick way to book recovery sessions, view their treatment history, and manage their profile.
* **First-Time Visitors:** Need to understand the types of therapy offered, see transparent pricing, and easily register for an account.

### User Stories

#### **Account Management & Navigation**
| Issue ID | User Story | Priority |
|----------|------------|----------|
| [#1](https://github.com/Inna-Kot/body_therapy_proj5/issues/1) | As a **Site Visitor** I can **register for a personal account** so that I can view my profile, order therapy sessions, and leave reviews. | MUST HAVE |
| [#2](https://github.com/Inna-Kot/body_therapy_proj5/issues/2) | As a **Registered User** I can **easily log in and out of my account** so that my personal information and order history are kept secure. | MUST HAVE |
| [#3](https://github.com/Inna-Kot/body_therapy_proj5/issues/3) | As a **Site User** I can **intuitively navigate the website from any device** so that I can easily find therapy services, my cart, and my profile. | MUST HAVE |
| [#17](https://github.com/Inna-Kot/body_therapy_proj5/issues/17)| As a **Registered User** I can **view my personal profile and order history** so that I can keep track of my past and upcoming therapy sessions. | SHOULD HAVE |

#### **Core Functionality (Therapy Services)**
| Issue ID | User Story | Priority |
|----------|------------|----------|
| [#5](https://github.com/Inna-Kot/body_therapy_proj5/issues/5) | As a **Site Visitor** I can **view a list of available therapy services** so that I can choose the right treatment for my needs. | MUST HAVE |
| [#6](https://github.com/Inna-Kot/body_therapy_proj5/issues/6) | As a **Site Visitor** I can **click on a specific therapy service** so that I can read a detailed description and proceed to booking/payment. | MUST HAVE |
| [#7](https://github.com/Inna-Kot/body_therapy_proj5/issues/7) | As a **Site Admin** I can **add, update, and delete therapy services directly from the website frontend** so that I can easily manage my practice offerings. | MUST HAVE |

#### **E-commerce & Booking (Stripe)**
| Issue ID | User Story | Priority |
|----------|------------|----------|
| [#8](https://github.com/Inna-Kot/body_therapy_proj5/issues/9) | As a **Site User** I can **view the contents of my cart and remove services** so that I have full control over what I am purchasing before payment. | MUST HAVE |
| [#9](https://github.com/Inna-Kot/body_therapy_proj5/issues/8) | As a **Site User** I can **add a therapy service to my cart (booking list)** so that I can review my selected sessions before proceeding to checkout. | MUST HAVE |
| [#10](https://github.com/Inna-Kot/body_therapy_proj5/issues/10)| As a **Site User** I can **securely enter my payment details and complete the purchase via Stripe** so that my booking is confirmed and my payment is processed safely. | MUST HAVE |

#### **Feedback & Marketing**
| Issue ID | User Story | Priority |
|----------|------------|----------|
| [#13](https://github.com/Inna-Kot/body_therapy_proj5/issues/13)| As a **Site Owner** I can **implement SEO best practices like meta tags, sitemap, and robots.txt** so that search engines can index my site and potential clients can find me. | MUST HAVE |
| [#14](https://github.com/Inna-Kot/body_therapy_proj5/issues/14)| As a **Site Visitor** I can **subscribe to the newsletter and follow social media links** so that I can stay updated on new therapy sessions and health tips. | MUST HAVE |

#### **Future Features (Out of Scope for Initial Release)**
| Issue ID | User Story | Priority |
|----------|------------|----------|
| [#4](https://github.com/Inna-Kot/body_therapy_proj5/issues/4) | As a **Site Visitor** I can log in using my Google or Facebook account. | FUTURE |
| [#15](https://github.com/Inna-Kot/body_therapy_proj5/issues/15)| As a **Client** I want to receive an automated SMS/email reminder 24 hours before my appointment. | FUTURE |
| [#16](https://github.com/Inna-Kot/body_therapy_proj5/issues/16)| As a **Regular Client** I want to purchase a package of 5 therapy sessions at a discounted rate. | FUTURE |
| [#11](https://github.com/Inna-Kot/body_therapy_proj5/issues/11)| As a **Registered User** I can **leave a review for a therapy session I attended** so that I can share my experience with others. | FUTURE |
| [#12](https://github.com/Inna-Kot/body_therapy_proj5/issues/12)| As a **Registered User** I can **edit or delete my own review** so that I can correct mistakes or remove my feedback. | FUTURE |

---

## Design

The design of the application is crafted to reflect professionalism, medical expertise, and trust, which are crucial for a private sports massage and injury recovery practice. 

### Color Scheme
The color palette is deliberately minimalist, focusing on high contrast and readability to ensure a premium user experience.
* **#000000 (Black) & #FFFFFF (White):** Form the core of the application, providing a clean, clinical, and highly professional contrast for the top banner, footer, and text.
* **#222222 (Dark Grey):** Used for interactive elements like the "Book a Session" button to create a subtle hover effect without breaking the monochrome elegance.
* **#002147 (Dark Blue) & #046307 (Dark Green):** Used strategically as text-shadow overlays (`rgba`) on hero images to improve text readability while subtly mirroring the brand colors found in the Vitaliy Body Therapy logo.

### Typography
* **Lato:** The primary font used throughout the application. It was chosen for its excellent readability across all devices and its modern, clean lines that suit a health and wellness platform. Text sizes and weights are varied (e.g., bold uppercase for headers) to create a clear information hierarchy.

### Imagery
* **Hero Backgrounds:** The site uses vintage anatomical drawings (e.g., the spine structure) as background imagery. This visual strategy immediately communicates a deep understanding of human anatomy and builds trust in the therapist's expertise.
* **Cloudinary:** All dynamic imagery and media are served efficiently via Cloudinary to ensure fast loading times.

### Wireframes
* *The wireframes for Desktop, Tablet, and Mobile views will be added upon the completion of all frontend pages to accurately reflect the final user interface.*

## Database Design

### Entity Relationship Diagram (ERD)
The following diagram illustrates the database schema and the relationships between the entities in the **Body Therapy** application.

![Database Schema](docs/database.png)

### Data Models

#### **Category** (`services` app)
Used to organise treatments into logical groups (e.g. Sports Massage, Spa & Wellness, Injury Recovery). Each category has a `name` and an optional `friendly_name` for display purposes.

#### **Service** (`services` app)
Stores detailed information about each treatment offered, including:
- `name`, `description`, `price`, `duration_minutes`, and `image`
- Therapy-specific fields: `preparation` (pre-session guidance) and `contraindications` (medical warnings)
- A `slug` field, automatically generated from the service name
- An optional `category` foreign key linking to `Category`

#### **Booking** (`booking` app)
The core of the appointment system. Records the date and time slot a registered user has booked for a specific service.
- Linked to both `User` (Django's built-in auth model) and `Service`
- `status` field tracks the booking lifecycle: Pending Payment, Confirmed, Completed, Cancelled
- `stripe_pid` stores the related Stripe payment intent ID
- Validation logic (`clean()`) prevents bookings on past dates or weekends
- A `unique_together` constraint on `booking_date`, `time_slot`, and `service` prevents double-booking the same slot

#### **Order** (`checkout` app)
Stores order and customer billing information for a completed checkout, including a unique, auto-generated `order_number`, contact details, and running totals (`order_total`, `grand_total`) calculated from its line items.

#### **OrderLineItem** (`checkout` app)
Represents a single booked service within an order. Stores the `service`, `quantity`, `booking_date`, `time_slot`, and the `lineitem_total` (calculated automatically from the service price at the time of purchase).

#### **Collaboration** (`collaborations` app)
Stores collaboration requests submitted by potential partners or organisations, including contact details, the type of collaboration requested (guest blog, workshop, partnership, etc.), a message, an optional file attachment, and a status field for tracking the request (New, Under Review, Accepted, Declined).

### Relationships Summary

* **One-to-Many**
  - `Category` can have multiple `Service` records.
  - `Service` can have multiple `Booking` and `OrderLineItem` records.
  - `User` can have multiple `Booking` records.
  - `Order` contains multiple `OrderLineItem` records.

* **Standalone**
  - `Collaboration` is a standalone model used to capture collaboration enquiries via a public form; it is not linked to other models.

## Technologies Used

### Languages
* HTML5
* CSS3
* JavaScript
* Python

### Frameworks & Libraries
* **Django** - the core web framework used to build the application.
* **Bootstrap 4** - used for responsive layout, navigation, and UI components.
* **Crispy Forms** - used to render Django forms with Bootstrap styling and validation feedback.
* **django-allauth** - provides user registration, login, logout, and email verification.

### Database
* **PostgreSQL** (hosted on [Neon.tech](https://neon.tech)) - the production relational database.

### APIs & External Services
* **Stripe** - handles secure online payment processing.
* **Cloudinary** - cloud storage for static and media files (images).
* **Brevo** - sends transactional emails (signup verification, collaboration requests) via its HTTP API.

### Deployment & Version Control
* **Render** - hosting platform for the deployed application.
* **Git & GitHub** - version control and repository hosting.

## Deployment

### Local Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Inna-Kot/body_therapy_proj5.git
   cd body_therapy_proj5
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # Windows (Git Bash)
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create an `env.py` file in the project root (this file is included in `.gitignore` and must never be committed) with the following environment variables:
   ```python
   import os

   os.environ["DEVELOPMENT"] = "True"
   os.environ["SECRET_KEY"] = "your-secret-key"
   os.environ["DATABASE_URL"] = "your-postgresql-database-url"
   os.environ["CLOUDINARY_URL"] = "your-cloudinary-url"
   os.environ["STRIPE_PUBLIC_KEY"] = "your-stripe-public-key"
   os.environ["STRIPE_SECRET_KEY"] = "your-stripe-secret-key"
   os.environ["STRIPE_CURRENCY"] = "eur"
   os.environ["BREVO_API_KEY"] = "your-brevo-api-key"
   ```

5. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser account (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Visit `http://127.0.0.1:8000/` in your browser.

---

### Database Setup (PostgreSQL via Neon.tech)

This project uses PostgreSQL, hosted on [Neon.tech](https://neon.tech), as its production database.

1. Create a free account at [Neon.tech](https://neon.tech).
2. Create a new project and database.
3. Copy the provided connection string (in the format `postgresql://user:password@host/dbname`).
4. Add this connection string as the `DATABASE_URL` environment variable, both locally (in `env.py`) and on Render (see below).
5. Run `python manage.py migrate` to create all required tables in the new database.

---

### Deployment to Render

This project is deployed on [Render](https://render.com) as a Web Service.

1. Create a new **Web Service** on Render and connect it to the GitHub repository.

2. Set the following configuration:
   - **Build Command:**
     ```
     pip install -r requirements.txt
     ```
   - **Start Command:**
     ```
     gunicorn body_therapy.wsgi
     ```

3. Add the following environment variables in the Render dashboard (Settings → Environment):

   | Variable | Description |
   |----------|-------------|
   | `SECRET_KEY` | Django secret key |
   | `DATABASE_URL` | PostgreSQL connection string (Neon.tech) |
   | `CLOUDINARY_URL` | Cloudinary API URL for static and media file storage |
   | `STRIPE_PUBLIC_KEY` | Stripe publishable key |
   | `STRIPE_SECRET_KEY` | Stripe secret key |
   | `STRIPE_CURRENCY` | Currency code used for Stripe payments (e.g. `eur`) |
   | `BREVO_API_KEY` | Brevo API key, used for sending transactional emails via the Brevo HTTP API (see [Bugs & Fixes](#bugs--fixes) for why this is required instead of SMTP) |
   | `PYTHON_VERSION` | Python version used by Render's build environment |

4. Deploy the service. Render will automatically rebuild and redeploy on every push to the connected branch.

5. After the first deployment, run database migrations on the production database. This can be done by temporarily setting the Start Command to:
   ```
   python manage.py migrate && gunicorn body_therapy.wsgi
   ```
   or by running migrations manually via the Render Shell.

6. Create a superuser on the production database via the Render Shell:
   ```bash
   python manage.py createsuperuser
   ```

---

### Security Notes

- `DEBUG` is controlled by the presence of a `DEVELOPMENT` environment variable (`DEBUG = 'DEVELOPMENT' in os.environ`). This variable is set locally in `env.py` but is **not** set on Render, so `DEBUG` automatically evaluates to `False` in production.
- All secret keys, API keys, and database credentials are stored as environment variables and are never committed to the repository (`env.py` is listed in `.gitignore`).
- Static and media files are served via Cloudinary, keeping the application stateless and ensuring uploaded images persist across deployments.

## Bugs & Fixes

### Email Configuration Fix (Render Deployment)

#### Problem
Email functionality (signup verification, collaboration requests) returned a `500 Internal Server Error` on Render in production, while working correctly in local development.

#### Diagnosis
Render logs revealed that the Gunicorn worker was hanging on `socket.connect()` during SMTP connection attempts, eventually triggering `WORKER TIMEOUT` and a `SIGKILL` of the worker process. This occurred consistently with both Gmail SMTP and Brevo's SMTP relay, on port 587.

**Root cause:** Render's free tier blocks all outbound connections on standard SMTP ports (25, 465, 587), regardless of the email provider used.

#### Solution
Replaced SMTP-based email sending with the Brevo HTTP API (REST API over HTTPS, port 443, which is not blocked by Render). Implemented a custom Django email backend (`BrevoAPIEmailBackend` in `body_therapy/email_backends.py`) that sends emails via `requests.post()` to `https://api.brevo.com/v3/smtp/email`, supporting both plain-text and HTML content.

#### Outlook-Specific Issue
A secondary issue emerged after the Brevo API fix: confirmation emails reached Outlook inboxes (in the Junk/Other folder), but the verification link displayed as plain unclickable text rather than a clickable link.

**Cause:** django-allauth's email confirmation templates only included plain-text (`.txt`) versions. Without an HTML alternative, the email backend sent text-only emails. Gmail auto-links plain URLs in text emails; Outlook does not.

**Fix:** Added HTML templates (`email_confirmation_message.html` and `email_confirmation_signup_message.html`) alongside the existing `.txt` templates, enabling Django to send multipart emails (`EmailMultiAlternatives`) with a properly rendered `<a href>` link.

#### Verification
Used Brevo's transactional email logs (delivery status, "Clicked links" tracking, and email content preview) to confirm both the text and HTML versions of each email were correctly generated and delivered.

#### Result
- Signup email verification works correctly on Render, including clickable links on Outlook
- Collaboration request emails work on Render and include the full form submission details (contact info, collaboration type, message)
- Solution is free, persistent, and independent of hosting tier

## Testing

Manual testing was carried out throughout development to verify functionality, usability, responsiveness, and data management across the application.

### Functional Testing

| Feature | Test Performed | Expected Result | Actual Result |
|---|---|---|---|
| User Registration | Sign up with a new email address | Account created, verification email sent | Pass |
| Email Verification | Click verification link in email (Gmail and Outlook) | Email confirmed, account activated | Pass |
| Login / Logout | Log in with valid credentials, then log out | User is authenticated/de-authenticated, navigation reflects login state | Pass |
| Service - Create | Add a new service via the admin-only "Add Service" form | New service saved and immediately visible on the home page | Pass |
| Service - Read | View a service's detail page | Correct service details displayed (description, price, preparation, contraindications) | Pass |
| Service - Update | Edit an existing service and save | Changes immediately reflected on the home page and detail page | Pass |
| Service - Delete | Delete a service (with confirmation dialog) | Confirmation prompt shown; on confirm, service removed from home page without errors | Pass |
| Non-admin access to Service Management | Attempt to access Add/Edit/Delete URLs as a non-superuser | User redirected to home page with an error message | Pass |
| Booking | Click "Book Now" on a service, select a valid date/time | Booking form loads with correct service details, date/time can be selected | Pass |
| Booking validation | Attempt to book a past date or a weekend date | Validation error displayed, booking is rejected | Pass |
| Stripe Checkout | Complete checkout using Stripe test card (4242 4242 4242 4242) | Payment processed in Stripe test mode, success message displayed to user | Pass |
| Collaboration Form | Submit the collaboration request form | Form data saved, confirmation email sent with all submitted details | Pass |
| 404 Page | Navigate to a non-existent URL | Custom 404 page displayed with a link back to the home page | Pass |

### Responsiveness Testing

Tested using Chrome DevTools device toolbar at 375px (Mobile), 768px (Tablet), and 1440px (Desktop), as well as on a physical iPhone device.

| Screen Size | Result |
|---|---|
| Desktop (1440px) | Layout displays correctly; navigation, hero section, and service listings are well-spaced and readable |
| Tablet (768px) | Known issue - see below |
| Mobile (375px) | Known issue - see below |

### Code Validation

- **HTML**: Validated using the [W3C Nu Html Checker](https://validator.w3.org/nu/). The home page, service detail pages, and login page pass with no errors. One known issue remains on the signup page (see below).
- **CSS**: Validated using the [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) - no errors found.
- **Python**: Code follows PEP8 styling conventions (checked with flake8).

### Known Issues

#### Header/Hero Overlap on Mobile and Tablet

On screen widths below 992px, the fixed-position header (navigation icons, hamburger menu) overlaps with the hero section heading ("The path to recovery starts here.") on initial page load. This is caused by the `.hero-image-container` using `height: 100vh` combined with the header's `position: fixed` behaviour switching to `position: relative` only above 992px (see `@media (max-width: 991.98px)` in `static/css/base.css`).

This does not affect functionality - all navigation links and buttons remain clickable - but it is a visual issue affecting the information hierarchy on smaller screens. This has been identified as a priority fix for a future iteration, by adjusting the hero section's top padding/margin within the relevant media query.

#### `<ul>` Inside `<small>` on Signup Page

The signup page (`/accounts/signup/`) produces one W3C validation error: an unordered list (password requirements) is rendered inside a `<small>` element by django-allauth's crispy-forms integration. This is generated by a third-party template and does not affect functionality or accessibility - password requirements are still announced to assistive technology. A full fix would require overriding allauth's internal field templates, which was deprioritised given the scope of this submission.

#### `<h6>` Dropdown Headers in Categories Menu

The Categories dropdown in the main navigation uses `<h6>` elements for category group headings (e.g. "Sports Massage", "Spa & Wellness"). The W3C validator raises a warning that the document has no heading with a computed level of 1, partly due to these `<h6>` elements appearing without a preceding `<h1>`-`<h5>` in that section of the document. This follows common Bootstrap dropdown conventions and does not affect functionality or screen reader navigation, but is noted here as a minor semantic deviation.