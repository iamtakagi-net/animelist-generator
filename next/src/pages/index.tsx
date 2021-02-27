import React, { useState } from "react";
import Head from "next/head";
import { useClient } from "../../hooks/client";
import { useToasts } from "react-toast-notifications"

const IndexPage = () => {
  const toast = useToasts()

  const [url, setUrl] = useState("");
  const [base64, setBase64] = useState("")
  const [isGenerating, setIsGenerating] = useState(false)
  const client = useClient()

  let image
  if (base64.length) {
    image = <img src={`data:image/png;base64,${base64}`} className="mt-3"/>
  }

  let statusText
  let button
  if (isGenerating) {
    button = null
    statusText = <p className="text-md">画像を生成しています...</p>
  } else {
    button = <button className="bg-gray-300 mt-2 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center" onClick={async () => {
      setIsGenerating(true)
      client.generate(url).then(data => {
        setBase64(data.base64str)
        setIsGenerating(false)
        toast.addToast("画像を生成しました", {
          appearance: "success",
          autoDismiss: true,
        })
      }).catch((error) => {
        setIsGenerating(false)
        toast.addToast("画像の生成に失敗しました", {
          appearance: "error",
          autoDismiss: true,
        })
      })
    }}>
      生成
    </button>
  }

  return (
    <>
      <Head>
        <title>AnimeList Generator</title>
        <meta property="og:title" content="AnimeList Generator" />
        <meta property="og:description" content="アニメリストを生成します" />
        <meta property="og:url" content="" />
        <meta property="og:image" content="" />
        <meta name="twitter:card" content="summary" />
      </Head>
      <div className="min-h-screen">
        <div className="container mx-auto h-screen flex justify-center text-center">
          <div className="w-2/3 mx-auto flex-col">
            <div className="desc w-full my-6 space-y-1">
              <p className="text-lg">AnimeList Generator</p>
              <p className="text-sm"> <a href="https://www.animatetimes.com/">アニメイトタイムズ</a> からデータを取得して画像を生成します</p>

              <div className="space-x-4 pt-1">

                <label className="block">
                  <span className="text-gray-700">URL</span>
                  <input type="text" className="form-input mt-1 block w-full" placeholder="e.g. https://www.animatetimes.com/tag/details.php?id=5228" defaultValue={url} onChange={event => setUrl(event.target.value)} />
                </label>

                {button}

                {statusText}

              </div>

            </div>

            {image}
          </div>
        </div>
      </div>
    </>
  )
}

export default IndexPage