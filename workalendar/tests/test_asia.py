from datetime import date
from workalendar.tests import GenericCalendarTest

from workalendar.asia import Qatar


class QatarTest(GenericCalendarTest):
    cal_class = Qatar

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 7, 9), holidays)  # start ramadan
        # warning, the official date was (2013, 8, 10)
        self.assertIn(date(2013, 8, 8), holidays)  # eid al fitr
        # The official date was (2013, 10, 14)
        self.assertIn(date(2013, 10, 15), holidays)  # eid al adha
        self.assertIn(date(2013, 10, 16), holidays)  # eid al adha
        self.assertIn(date(2013, 10, 17), holidays)  # eid al adha
        self.assertIn(date(2013, 10, 18), holidays)  # eid al adha
        self.assertIn(date(2013, 12, 18), holidays)  # National Day

    def test_weekend(self):
        # In Qatar, Week-end days are Friday / Sunday.
        weekend_day = date(2017, 5, 12)  # This is a Friday
        non_weekend_day = date(2017, 5, 14)  # This is a Sunday
        self.assertFalse(self.cal.is_working_day(weekend_day))
        self.assertTrue(self.cal.is_working_day(non_weekend_day))
