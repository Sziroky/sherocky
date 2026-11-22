import data from '../data/concerts.json';

export type Gig = { date: string; title: string; place: string; link: string | null; private: boolean };

const all = (data.events as Gig[]).slice().sort((a, b) => a.date.localeCompare(b.date));
// Podgląd: liczone w momencie budowania. Docelowo: dane z Kalendarza Google odświeżane na serwerze.
const now = new Date().toISOString().slice(0, 16);

export const upcoming = () => all.filter(g => g.date >= now);
export const past = () => all.filter(g => g.date < now).reverse();
export const isExample = Boolean((data as { isExample?: boolean }).isExample);

const months = ['sty', 'lut', 'mar', 'kwi', 'maj', 'cze', 'lip', 'sie', 'wrz', 'paź', 'lis', 'gru'];
export const fmtDate = (iso: string) => {
  const d = new Date(iso);
  return `${d.getDate()} ${months[d.getMonth()]} ${d.getFullYear()}`;
};
export const parts = (iso: string) => {
  const d = new Date(iso);
  return { day: String(d.getDate()).padStart(2, '0'), mon: months[d.getMonth()], year: d.getFullYear(), time: iso.slice(11, 16) };
};
