# IMMO Website Backend

## Overview

This is the backend of a realstate web application built using **Flask**, a Python web framework. The API manages announcements, user messages, user data, and administration tasks. The backend uses **MySQL** as the database management system (DBMS) and **SQLAlchemy** as the ORM (Object-Relational Mapping).

## Announce Routes

### Get All Announcements

```python
GET /ok
```

Retrieves a list of all announcements.

### Get Announcement Details

```python
GET /<annonceId>
```

Retrieves details of a specific announcement identified by `annonceId`.

### Add Announcement

```python
POST /
```

Adds a new announcement. Requires authentication.

### Delete Announcement

```python
DELETE /<annonceId>
```

Deletes a specific announcement identified by `annonceId`. Requires authentication.

### Search for Announcement

```python
GET /search
```

Searches for announcements.

### Get Announcement Types

```python
GET /types
```

Retrieves a list of announcement types.

## My Announcements Routes

### Get User Announcements

```python
GET /
```

Retrieves announcements associated with the authenticated user. Requires authentication.

## Message Routes

### Get All Messages

```python
GET /
```

Retrieves all messages for the authenticated user. Requires authentication.

### Get Unseen Messages Count

```python
GET /unseen
```

Retrieves the count of unseen messages for the authenticated user. Requires authentication.

### View Message

```python
PUT /view
```

Marks a message as viewed. Requires authentication.

### Send Message

```python
POST /
```

Sends a new message. Requires authentication.

## User Routes

### Get All Users

```python
GET /
```

Retrieves a list of all users.

### Login

```python
POST /
```

Logs in a user.

### Fill User Data

```python
PUT /user
```

Fills in user data. Requires authentication.

### Check User Validity

```python
GET /<userId>
```

Checks if the user is valid based on address presence. Requires authentication.

## Admin Routes

### Scrap Announcements

```python
GET /scrap
```

Scrapes announcements data. Admin access required.

### Get Website Stats

```python
GET /stats
```

Retrieves website statistics. Admin access required.

## Installation

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up the MySQL database and update the configuration in `config.py`.
4. Run the application using `python app.py`.

## Contributing

Feel free to contribute to the development of this web application backend. Create a fork of the repository, make your changes, and submit a pull request.
