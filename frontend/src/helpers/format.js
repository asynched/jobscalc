import { differenceInDays } from 'date-fns'

export const formatValue = (value) => value.toFixed(2).replace('.', ',')

export const evaluateAndFormatDate = (date) => {
  const parsedDate = new Date(Date.parse(date + ' 00:00'))

  const now = new Date(Date.now())

  const difference = differenceInDays(parsedDate, now)

  return difference
}
