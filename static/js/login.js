/*******************************************************************
 * ログインクラス
 ********************************************************************/

var Login = {};

/** 
 * 超簡易ログイン認証
 * @param loginForm formエレメント
 * @return 成功時true,失敗時false
 */
Login.doLogin = function doLogin(loginForm) {
    //空チェック
    if(loginForm.id.value == '') {
        return Login.doError('ユーザー名を入力してください。');
    }
    if(loginForm.password.value == '') {
        return Login.doError('パスワードを入力してください。');
    }

    //エラーなし
    return true;
}

/**
 * エラー時の動作
 * @param msg エラーメッセージ
 * @return falseを返す
 */
Login.doError = function doError(msg) {
    alert(msg);
    return false;
}
