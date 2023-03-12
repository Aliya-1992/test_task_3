import pytest
from validators.validator import Validator


class TestT:

    @pytest.mark.parametrize(
        'iter_number',
        [i for i in range(1, 6)],
        ids=lambda iter_number: f'Number of iteration: {iter_number}'
    )
    def test_registration_page(self, registration_page_router, get_driver, iter_number):
        registration_page_router.registration_page()
        if iter_number < 5:
            get_driver.back()
        Validator.assertion(registration_page_router.get_status_code(), 201)
