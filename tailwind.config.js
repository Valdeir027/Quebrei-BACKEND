/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html,js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}

