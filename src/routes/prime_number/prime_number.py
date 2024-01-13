from fastapi import APIRouter


def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


prime_number_router = APIRouter()


@prime_number_router.get("/check-prime/{number}")
async def check_prime_number(number: int):
    if is_prime_number(number):
        return {"result": f"{number} jest liczbą pierwszą."}
    else:
        return {"result": f"{number} nie jest liczbą pierwszą."}
