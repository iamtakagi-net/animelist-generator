import React, { useState } from "react";
import { useClient } from "../hooks/client";
import { useToasts } from "react-toast-notifications";
import ThemeSwitch from "../components/ThemeSwitch";
import { Animelist } from "../types/animelist";

const IndexPage = () => {
  const toast = useToasts();

  const [url, setUrl] = useState<string>("")
  const [animelist, setAnimelist] = useState<Animelist | null>(null)
  const [isGenerating, setIsGenerating] = useState(false);
  const client = useClient();

  let image;
  let downloadButton;
  if (animelist && animelist.base64Str && animelist.title) {
    image = (
      <img
        src={`data:image/png;base64,${animelist.base64Str}`}
        className="mt-3"
      />
    );
    downloadButton = (
      <a
        className="bg-gray-300 mt-2 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center"
        href={`data:image/png;base64,${animelist.base64Str}`}
        download={`${animelist.title}.png`}
      >
        ダウンロード
      </a>
    );
  }

  let statusText;
  let button;
  if (isGenerating) {
    button = null;
    downloadButton = null;
    image = null;
    statusText = <p className="text-md">画像を生成しています...</p>;
  } else {
    button = (
      <button
        className="bg-gray-300 mt-2 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center"
        onClick={async () => {
          setIsGenerating(true);
          client
            .generate(url)
            .then((data) => {
              setAnimelist(data);
              setIsGenerating(false);
              toast.addToast("画像を生成しました", {
                appearance: "success",
                autoDismiss: true,
              });
            })
            .catch((error) => {
              setIsGenerating(false);
              toast.addToast("画像の生成に失敗しました", {
                appearance: "error",
                autoDismiss: true,
              });
            });
        }}
      >
        生成
      </button>
    );
  }

  return (
    <div className="container mx-auto h-screen flex justify-center text-center">
      <div className="w-2/3 mx-auto flex-col">
        <div className="mt-5">
          <ThemeSwitch />
        </div>

        <div className="desc w-full my-6 space-y-1">
          <p className="text-lg">AnimeList Generator</p>
          <p className="text-sm">
            {" "}
            <a href="https://www.animatetimes.com/">アニメイトタイムズ</a>{" "}
            から取得したデータをもとに画像を生成します
          </p>

          <div className="space-x-4 pt-1">
            <label className="block">
              <span className="text-gray-700">URL</span>
              <input
                type="text"
                className="form-input mt-1 block w-full"
                placeholder="e.g. https://www.animatetimes.com/tag/details.php?id=5228"
                defaultValue={url}
                onChange={(event) => setUrl(event.target.value)}
              />
            </label>

            {button}

            {downloadButton}

            {statusText}
          </div>
        </div>

        {image}
      </div>
    </div>
  );
};

export default IndexPage;
