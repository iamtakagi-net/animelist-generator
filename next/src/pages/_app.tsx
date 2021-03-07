import * as React from 'react'
import Router from 'next/router'
import { AppProps } from 'next/app'
import { ToastProvider } from "react-toast-notifications";

import "../styles/main.css";

const App: React.FC<AppProps> = ({ Component, pageProps }) => {
  return (
    <ToastProvider>
      <Component {...pageProps} />
    </ToastProvider>
  );
}

export default App
