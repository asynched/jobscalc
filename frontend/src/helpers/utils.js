import { format, addDays } from "date-fns";

export const setPageTitle = (pageName) => {
  document.title = `JobsCalc | ${pageName}`;
};

export const getDefaultDate = () => {
  const now = new Date(Date.now());
  const sevenDaysLater = addDays(now, 7);
  const value = format(sevenDaysLater, "yyyy-MM-dd");

  return value;
};
