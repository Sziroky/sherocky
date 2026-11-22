// Linki wewnętrzne z uwzględnieniem bazowej ścieżki (np. /sherocky na GitHub Pages).
const base = import.meta.env.BASE_URL.replace(/\/$/, '');
export const u = (path: string) => base + path;
