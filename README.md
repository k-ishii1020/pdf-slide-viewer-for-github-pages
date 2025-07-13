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
  - F: フルスクリーンモード
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

