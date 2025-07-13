# PDF Slide Viewer for GitHub Pages

A utility that allows you to upload PDF slide materials to your own repository and view them on the web by deploying them as GitHub Pages.  
While there are many services available for publishing slide materials, you can easily publish them at zero cost by utilizing GitHub Pages.

A notable feature is that external URLs embedded in the slides are clickable.

## 📋 Features

- **PDF Link Support**: External URLs embedded in PDFs are clickable
- **Responsive Design**: Mobile and desktop compatible
- **Keyboard Shortcuts**:
  - Left/Right arrow keys: Navigate pages
  - F: Fullscreen mode(Only supported in PC browsers)
- **Mouse Controls**:
  - Click left half of slide: Previous page
  - Click right half of slide: Next page

## ⚙ Initial Setup
1. Ensure Python is installed.  
   No special packages are required as only standard libraries are used.
1. Fork this repository.
1. Enable GitHub Pages:
   - Go to repository Settings > Pages > Source and set to "Deploy from a branch"
   - Select `main` branch and `/ (root)`
   - Click Save
   - Your GitHub Pages URL will be `https://<username>.github.io/<repository-name>/`
   - ⚠️ For free accounts, GitHub Pages is only available for Public repositories and can only be enabled for one repository.

1. Clone the repository locally:
   ```bash
   git clone https://github.com/k-ishii1020/pdf-slide-viewer-for-github-pages.git
   ```

## 📁 Adding New Materials
1. Add PDF files to the `pdf/` folder (please delete sample.pdf)

1. Generate the slide list:
   ```bash
   python3 generate_file_list.py
   ```
   Alternatively, you can manually edit `./pdf-files.js` to add PDF file information.
1. After merging to the main branch, GitHub Pages will update within a few minutes.

## 🔧 Local Development
```bash
# Start local server
./start_server.sh

# Open in browser
open http://localhost:8000
```

## 📄 License
This project is licensed under the Apache License 2.0.
See the [LICENSE](LICENSE) file for details.

## About Donations
If you find this project helpful, please consider supporting via the following link:
https://github.com/sponsors/k-ishii1020

---

# PDF スライドビューアー for GitHub Pages

PDF化されたスライド資料をご自身のリポジトリ上にアップロードし、GitHub Pagesとしてデプロイすることで  
スライド資料をWEB上で閲覧できるユーティリティです。  
世の中にスライド資料の公開が可能なサービスは多くありますが、GitHub Pagesを活用することでコストゼロで簡単に公開できます。

特にスライドの中に埋め込まれた外部URLをクリックできることが特徴です。

## 📋 機能

- **PDFリンク対応**: PDFに埋め込まれた外部URLがクリック可能。
- **レスポンシブデザイン**: モバイル・デスクトップ対応
- **キーボードショートカット**:
  - 左/右矢印キー: ページ移動
  - F: フルスクリーンモード(PCブラウザのみ対応)
- **マウス操作**:
  - スライドの左半分をクリック: 前のページ
  - スライドの右半分をクリック: 次のページ

## ⚙ 初期セットアップ
1. Pythonがインストールされていることを確認してください。  
標準ライブラリのみを使用しているため、特別なパッケージは必要ありません。
1. このリポジトリをForkします。
1. GitHub Pagesを有効化します。
   - リポジトリの設定(Settings) > Pages > Sourceを「Deploy from a branch」に設定
   - Branchは `main` を選択し、 `/ (root)` を選択
   - Saveをクリック
   -  GitHub PagesのURLは `https://<username>.github.io/<repository-name>/` になります。
   - ⚠️無課金アカウントの場合、GitHub PagesはPublicリポジトリでのみ利用可能かつ1つのリポジトリに対してのみ有効です。

1. リポジトリをローカル上にクローンします。
    ```bash
    git clone https://github.com/k-ishii1020/pdf-slide-viewer-for-github-pages.git
    ```

## 📁 新しい資料の追加方法
1. pdfファイルを `pdf/` フォルダに追加します。（sample.pdfは削除してください）

1. スライドリストを生成します。  
   ```bash
   python3 generate_file_list.py
   ```
   あるいは、手動で `./pdf-files.js` を編集して、PDFファイルの情報を追加することも可能です。
1. mainブランチにマージされると、数分でGitHub Pagesが更新されます。



## 🔧 ローカルでの動作確認方法
```bash
# ローカルサーバー起動
./start_server.sh

# ブラウザで開く
open http://localhost:8000
```

## 📄 ライセンス
このプロジェクトはApache License 2.0の下でライセンスされています。
詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 寄付について
もしこのプロジェクトが役立ったと感じたら、以下のリンクから寄付を検討していただけると幸いです。
https://github.com/sponsors/k-ishii1020

