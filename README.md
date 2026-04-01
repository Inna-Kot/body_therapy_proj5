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
* **Site Owner (Private Therapist):** Needs to manage service offerings, track bookings, and build trust through client reviews.
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
| [#11](https://github.com/Inna-Kot/body_therapy_proj5/issues/11)| As a **Registered User** I can **leave a review for a therapy session I attended** so that I can share my experience with others. | SHOULD HAVE |
| [#12](https://github.com/Inna-Kot/body_therapy_proj5/issues/12)| As a **Registered User** I can **edit or delete my own review** so that I can correct mistakes or remove my feedback. | SHOULD HAVE |
| [#13](https://github.com/Inna-Kot/body_therapy_proj5/issues/13)| As a **Site Owner** I can **implement SEO best practices like meta tags, sitemap, and robots.txt** so that search engines can index my site and potential clients can find me. | MUST HAVE |
| [#14](https://github.com/Inna-Kot/body_therapy_proj5/issues/14)| As a **Site Visitor** I can **subscribe to the newsletter and follow social media links** so that I can stay updated on new therapy sessions and health tips. | MUST HAVE |

#### **Future Features (Out of Scope for Initial Release)**
| Issue ID | User Story | Priority |
|----------|------------|----------|
| [#4](https://github.com/Inna-Kot/body_therapy_proj5/issues/4) | As a **Site Visitor** I can log in using my Google or Facebook account. | FUTURE |
| [#15](https://github.com/Inna-Kot/body_therapy_proj5/issues/15)| As a **Client** I want to receive an automated SMS/email reminder 24 hours before my appointment. | FUTURE |
| [#16](https://github.com/Inna-Kot/body_therapy_proj5/issues/16)| As a **Regular Client** I want to purchase a package of 5 therapy sessions at a discounted rate. | FUTURE |

---

## Technologies Used

* **Languages:** HTML5, CSS3, JavaScript, Python.
* **Framework:** Django.
* **Database:** PostgreSQL (Neon.tech).
* **Cloud Storage:** Cloudinary (for static and media files).
* **Payment Processing:** Stripe.
* **Deployment:** Render.
* **Version Control:** Git & GitHub.