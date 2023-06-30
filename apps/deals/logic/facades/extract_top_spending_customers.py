from apps.deals.logic.dto import ResponseSpendingCustomersDto, SpendingCustomersDto
from apps.deals.logic.selectors import extract_gem_names, extract_top_five_customers


def extract_top_spending_customers() -> dict[str, list[dict[str, str | int]]]:
    """Возвращает списк из 5 клиентов, потративших наибольшую сумму за весь период."""
    top_customers = extract_top_five_customers()

    response_list = []
    for customer in top_customers:
        gems = extract_gem_names(customers=top_customers, current_customer=customer.get('customer__username'))
        response_list.append(
            SpendingCustomersDto(
                username=customer.get('customer__username'), spent_money=customer.get('spent_money'), gems=list(gems)
            )
        )
    return ResponseSpendingCustomersDto(response=response_list).dict()
