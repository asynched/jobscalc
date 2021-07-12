export function calculateHourlyValue(
  monthlyPayment,
  worktimeDaily,
  worktimeWeekly,
  vacationWeeks
) {
  const WEEKS_PER_YEAR = 52
  const WEEKS_PER_MONTH = (WEEKS_PER_YEAR - vacationWeeks) / 12
  const WEEK_TOTAL_HOURS = worktimeDaily * worktimeWeekly

  const MONTHLY_TOTAL_HOURS = WEEK_TOTAL_HOURS * WEEKS_PER_MONTH || 1

  const HOURLY_VALUE = monthlyPayment / MONTHLY_TOTAL_HOURS

  return HOURLY_VALUE
}
