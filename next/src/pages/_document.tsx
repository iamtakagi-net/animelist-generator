import * as React from "react";
import NextDocument, {
  Html,
  Head,
  Main,
  NextScript,
  DocumentContext,
} from "next/document";

class Document extends NextDocument {
  static async getInitialProps(context: DocumentContext) {
    const initialProps = await NextDocument.getInitialProps(context);
    return { ...initialProps };
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
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}

export default Document;
