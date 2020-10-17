class SubscriptionConstants:
    class SubscriptionPeriods:
        WEEK = 1
        MONTH = 2
        YEAR = 3
        LIFETIME = 4

        PERIOD = (
            (WEEK, 'Тиждень'),
            (MONTH, 'Місяць'),
            (YEAR, 'Рік'),
            (LIFETIME, 'Довічно'),
        )

    class PaymentStatuses:
        PASSED = 1
        FAILED = 2
        PENDING = 3
        VERIFYING = 4

        STATUS = (
            (PASSED, 'Успішний'),
            (FAILED, 'Провал'),
            (PENDING, 'Очікування'),
            (VERIFYING, 'Перевірка'),
        )

    class SubscriptionStatuses:
        OK = 1
        INACTIVE = 2
        TRIAL = 3
        GRACE = 4
        NON_COMMERCIAL = 5
        PENDING = 6

        STATUS = (
            (OK, 'OK'),
            (INACTIVE, 'Деактивована'),
            (TRIAL, 'Пробний період'),
            (GRACE, 'Очікування продовження'),
            (NON_COMMERCIAL, 'Не комерційна'),
            (PENDING, 'В процесі оплати'),
        )

    class SubscriptionPlanCodes:
        FREE = 1
        BUSINESS = 2
        BUSINESS_PLUS = 3
        NON_COMERCIAL = 4

        STATUS = (
            (FREE, 'Безкоштовний'),
            (BUSINESS, 'Бізнес'),
            (BUSINESS_PLUS, 'Бізнес +'),
            (NON_COMERCIAL, 'Некомерційний'),
        )


class CompareConstants:
    WORSE = 1
    SAME = 2
    BETTER = 3

    STATUS = (
        (WORSE, 'Однаковий'),
        (SAME, 'Такий же'),
        (BETTER, 'Краще'),
    )
