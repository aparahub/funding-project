/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        montserrat: ['Montserrat', 'sans-serif'],
      },
      colors: {
        quizBg: '#FFFFEF',
        quizQuestion: '#D9594C',
        quizOption: '#6C8C7D',
        quizScore: '#F8C60F',
      },
    },
  },
  plugins: [],
}
