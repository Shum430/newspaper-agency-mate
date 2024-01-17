# Newspaper Agency Mate Deployment on Render

I am excited to announce the deployment of my Newspaper Agency Mate project on Render! You can access the live site [here](https://newspaper-agency-sbpa.onrender.com/).

## Project Details
- **Site Link:** [Newspaper Agency Mate](https://newspaper-agency-sbpa.onrender.com/)
- **GitHub Repository:** [newspaper-agency-mate](https://github.com/Shum430/newspaper-agency-mate)

## Installation Guide
Make sure you have Python 3 installed on your system before proceeding with the installation.

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Shum430/newspaper-agency-mate
    cd newspaper-agency-mate
    ```

2. **Set up a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    # OR
    venv\Scripts\activate  # For Windows
    ```

3. **Install the project dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## User Registration and Login
1. Visit the [site link](https://newspaper-agency-sbpa.onrender.com/).
2. Click on the "Login" button.
3. Register with the following data:
    - Username: user
    - Password: user12345
4. Click the registration button.

![Registration](img_1.png)

5. You have successfully logged in. Feel free to explore and utilize our services.

![Login](img_2.png)
![img_3.png](img_3.png)

## Features
- **Authentication Functionality:** Register and log in as a Redactor or User.
- **Website Interface:** Manage newspapers, topics, and redactors through an intuitive web interface.
- **Admin Panel:** Advanced management capabilities for administrators.
## Database Schema

### `Topic` Model:
- **Description:** Represents a topic or category that can be associated with one or more newspapers.
- **Relationships:**
  - **None explicitly defined in this model.**

### `Redactor` Model (Extending AbstractUser):
- **Description:** Represents a user with additional attributes, specifically tailored for redactors (journalists or writers).
- **Relationships:**
  - **None explicitly defined in this model.**
  - **Inherits relationships from `AbstractUser`.**

### `Newspaper` Model:
- **Description:** Represents a newspaper article.
- **Relationships:**
  - **`topic`:** ForeignKey relationship to the `Topic` model.
    - **Type:** Many-to-One (Each newspaper belongs to one topic, but a topic can have multiple newspapers).
    - **Field:** `topic` is a foreign key that establishes this relationship.
  - **`redactors`:** ManyToManyField relationship to the user model (`settings.AUTH_USER_MODEL`).
    - **Type:** Many-to-Many (Each newspaper can have multiple redactors, and each redactor can be associated with multiple newspapers).
    - **Field:** `redactors` is a many-to-many field that establishes this relationship.

### Summary of Relationships:
- A `Topic` can be associated with multiple `Newspaper` instances, but each `Newspaper` belongs to one `Topic`.
- A `Redactor` (user) can be associated with multiple `Newspaper` instances, and each `Newspaper` can have multiple `Redactor` contributors.

In summary, the relationships allow for the categorization of newspapers into topics, and multiple redactors can contribute to and be associated with each newspaper. The `ManyToManyField` in the `Newspaper` model facilitates a many-to-many relationship between newspapers and redactors.


We hope you enjoy using Newspaper Agency Mate! If you encounter any issues or have suggestions, feel free to contribute to our [GitHub repository](https://github.com/Shum430/newspaper-agency-mate).
