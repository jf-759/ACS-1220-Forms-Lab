from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, TextAreaField, URLField
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError, URL, Optional
from books_app.models import Audience, Book, Author, Genre

class BookForm(FlaskForm):
    """Form to create a book."""
    title = StringField('Book Title', 
        validators=[
            DataRequired(), 
            Length(min=3, max=80, message="Your message needs to be betweeen 3 and 80 chars")
        ])
    publish_date = DateField('Date Published', validators=[DataRequired()])
    author = QuerySelectField('Author', query_factory=lambda: Author.query, allow_blank=False)
    audience = SelectField('Audience', choices=Audience.choices())
    genres = QuerySelectMultipleField('Genres', query_factory=lambda: Genre.query)
    submit = SubmitField('Submit')

    def validate_title(form, field):
        if 'banana' in field.data:
            raise ValidationError('Title cannot contain the word banana')


class AuthorForm(FlaskForm):
    """Form to create an author."""

    name= StringField('Name', validators=[DataRequired(), Length(min=3, max=80)])
    biography = TextAreaField('Biography', validators=[DataRequired()])
    submit = SubmitField('Submit')

    # STRETCH CHALLENGE: Add more fields here as well as in `models.py` to
    # collect more information about the author, such as their birth date,
    # country, etc.

    birth_date = DateField('Birth Date', validators=[Optional()])
    death_date = DateField('Death Date', validators=[Optional()])
    country = StringField('Country of Origin', validators=[Optional(), Length(max=80)])
    website = URLField('Personal Website', validators=[Optional(), URL()])
    awards = TextAreaField('Notable Awards', validators=[Optional()])

    submit = SubmitField('Submit')

class GenreForm(FlaskForm):
    """Form to create a genre."""

    name = StringField('Genre Name', validators=[DataRequired(), Length(min=3, max=50)])
    submit = SubmitField('submit')
