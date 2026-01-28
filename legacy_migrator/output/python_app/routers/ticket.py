from fastapi import APIRouter
from models.ticket import *
from services.ticket_service import TicketService

router = APIRouter()

service = TicketService()

@router.get('/tickets')
def get_all_tickets():
    return {'status': 'ok'}

@router.post('/tickets')
def create_a_new_ticket():
    return {'status': 'ok'}

@router.put('/tickets/{id}/status')
def update_the_status_of_a_ticket():
    return {'status': 'ok'}
