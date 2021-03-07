import * as React from 'react'
import NextDocument, {
  Html,
  Head,
  Main,
  NextScript,
  DocumentContext,
} from 'next/document'

class Document extends NextDocument {
  static async getInitialProps(context: DocumentContext) {
    const initialProps = await NextDocument.getInitialProps(context)
    return { ...initialProps }
  }

  render() {
    return (
      <Html lang="en">
        <Head>
          <meta charSet="utf-8" />
          <meta
            name="viewport"
            content="initial-scale=1.0, width=device-width"
          />
          <link
            href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;800&display=swap"
            rel="stylesheet"
          />

          <title>AnimeList Generator</title>
          <meta property="og:title" content="AnimeList Generator" />
          <meta property="og:description" content="アニメリストを生成します" />
          <meta property="og:url" content="" />
          <meta property="og:image" content="" />
          <meta name="twitter:card" content="summary" />
        </Head>
        <body className="min-h-screen">
          <script
            dangerouslySetInnerHTML={{
              __html: `
                (function() {
                  let storageKey = 'darkMode';
                  let classNameDark = 'dark-mode';
                  let classNameLight = 'light-mode';
                
                  function setClassOnDocumentBody(darkMode) {
                    document.body.classList.add(darkMode ? classNameDark : classNameLight);
                    document.body.classList.remove(darkMode ? classNameLight : classNameDark);
                  }
                  
                  let preferDarkQuery = '(prefers-color-scheme: dark)';
                  let mql = window.matchMedia(preferDarkQuery);
                  let supportsColorSchemeQuery = mql.media === preferDarkQuery;
                  let localStorageTheme = null;
                  try {
                    localStorageTheme = localStorage.getItem(storageKey);
                  } catch (err) {}
                  let localStorageExists = localStorageTheme !== null;
                  if (localStorageExists) {
                    localStorageTheme = JSON.parse(localStorageTheme);
                  }
                
                  if (localStorageExists) {
                    setClassOnDocumentBody(localStorageTheme);
                  } else if (supportsColorSchemeQuery) {
                    setClassOnDocumentBody(mql.matches);
                    localStorage.setItem(storageKey, mql.matches);
                  } else {
                    var isDarkMode = document.body.classList.contains(classNameDark);
                    localStorage.setItem(storageKey, JSON.stringify(isDarkMode));
                  }
                })();
              `,
            }}
          />
          <Main />
          <NextScript />
        </body>
      </Html>
    )
  }
}

export default Document