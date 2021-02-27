import React from "react";
import type { AppProps } from "next/app";
import "../styles/index.css";
import { ToastProvider } from "react-toast-notifications";

function App({ Component, pageProps }: AppProps) {
  return (
      <ToastProvider>
           <Component {...pageProps} />
      </ToastProvider>
  )
}

export default App;