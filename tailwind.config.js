/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./js/**/*.js"
  ],
  theme: {
    extend: {
      screens: {
        xs: '380px'
      },
      fontFamily: {
        display: ['"Outfit"', 'sans-serif'],
        sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
        serif: ['"Instrument Serif"', 'serif'],
        mono: ['"JetBrains Mono"', 'monospace']
      },
      colors: {
        forest: {
          depths: '#122314',
          elevated: '#182E1B',
          surface: '#1F3823'
        },
        moss: {
          shadow: '#273f2b'
        },
        lichen: {
          sage: '#7e8371'
        },
        pale: {
          fern: '#b7bda5'
        },
        sprout: {
          DEFAULT: '#68ef3f',
          wash: '#e7f9dd',
          verdant: '#26a200'
        },
        mist: {
          green: '#d9deca'
        },
        onyx: {
          olive: '#30322a'
        },
        bone: {
          white: '#f2f5eb'
        },
        soft: {
          mist: '#dcdfe3'
        },
        cool: {
          stone: '#d6d6d6'
        },
        carbon: '#222222',
        pure: {
          white: '#ffffff'
        }
      }
    }
  },
  plugins: []
};
