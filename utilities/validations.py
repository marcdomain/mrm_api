import datetime
import validators
import re

from api.location.models import CountryType, TimeZoneType
from graphql import GraphQLError
from api.office_structure.models import OfficeStructure as OfficeStructureModel
from api.structure.models import Structure as StructureModel


def validate_url(**kwargs):
    """
    Function to validate url when
    saving an object
    :params kwargs
    """
    if not validators.url(kwargs.get('image_url')):
        raise AttributeError("Please enter a valid image url")


def validate_empty_fields(**kwargs):
    """
    Function to validate empty fields when
    saving an object
    :params kwargs
    """
    for field in kwargs:
        value = kwargs.get(field)
        if isinstance(value, str):
            value = value.strip()
        if not type(value) is bool and not value:
            raise AttributeError(field + " is required field")


def validate_date_time_range(**kwargs):
    """
    Function to validate the dates entered
    for questions for feedback
    :params kwargs
    """
    if ('start_date' and 'end_date' in kwargs) and\
            kwargs['start_date'] < datetime.datetime.now():
        raise ValueError('startDate should be today or after')
    elif ('start_date' and 'end_date' in kwargs) and\
            kwargs['end_date'] - kwargs['start_date'] < datetime.timedelta(
                days=1
    ):
        raise ValueError(
            'endDate should be at least a day after startDate'
        )


def validate_country_field(**kwargs):
    """
    Function to validate country fields when
    saving an object
    :params kwargs
    """
    valid_countries = [country.value for country in CountryType]
    country_name = kwargs['country']
    if country_name not in valid_countries:
        raise AttributeError("Not a valid country")


def validate_timezone_field(**kwargs):
    """
    Function to validate timezone fields when
    saving an object
    :params kwargs
    """
    timezones = [timezone.name for timezone in TimeZoneType]
    time_zone = kwargs['time_zone']
    if time_zone not in timezones:
        raise AttributeError("Not a valid time zone")


def validate_parent_node_id(parent_id):
    """
    Function to validate Parent node ID
    when creating child node
    """
    parent_node = OfficeStructureModel.query.filter_by(id=parent_id).first()
    if not parent_node:
        raise GraphQLError("Parent node ID Provided does not exist")


def validate_question_type(**kwargs):
    """
    Function to validate the question types,
    should allow only check, input and rate
    :params kwargs
    """
    question_types = ['check', 'input', 'rate']
    if 'question_type' in kwargs:
        type = kwargs['question_type']
        if type.lower() not in question_types:
            raise AttributeError("Not a valid question type")


def validate_date_range(**kwargs):
    """
    Function to validate the date range
    :params kwargs
    """
    if (('end_date' and 'start_date' in kwargs) and
        kwargs['end_date'] > datetime.datetime.now() or
            kwargs['start_date'] > datetime.datetime.now()):
        raise ValueError('Dates should be before today')
    elif (('end_date' and 'start_date' in kwargs) and
            kwargs['end_date'] < kwargs['start_date']):
        raise ValueError('Earlier date should be lower than later date')


def validate_room_labels(**kwargs):
    """
    Function to validate the room label string type
    :params room_labels
    """
    room_labels = kwargs.get('room_labels')
    new_label = re.search("[{}:]", str(room_labels))
    if new_label:
        raise AttributeError("Room label is not a valid string type")
    for i in room_labels:
        structure = StructureModel.query.filter_by(name=i).first()
        structure_name = None
        if structure:
            structure_name = structure.name
            break
        if not structure_name:
            raise GraphQLError("Structure does not exist")
