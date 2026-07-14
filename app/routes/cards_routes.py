from uuid import UUID

from fastapi import APIRouter,status, Depends

from models.cards_models import CardCreate, CardResponse
from services.cards_service import CardServices
from security.auth_bearer import get_current_user

router = APIRouter(prefix="/cards", tags=["Cards"])

@router.post("/", response_model=CardResponse, status_code=status.HTTP_201_CREATED)
def issue_card(data: CardCreate, current_user = Depends(get_current_user)) -> CardResponse:
    return CardServices.issue_card(current_user.id, data)

@router.get("/", response_model=list[CardResponse])
def list_cards(current_user = Depends(get_current_user)) -> list[CardResponse]:
    return CardServices.get_user_cards(current_user.id)