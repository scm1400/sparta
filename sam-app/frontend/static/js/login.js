let gUrl = "https://xec02xqv72.execute-api.ap-northeast-2.amazonaws.com/Prod";

function show_login_modal() {
    tmp_html = `<div class="modal is-active">
                                <div class="modal-background" onclick="close_modal()"></div>
                                <div class="modal-content" style="width: 500px; height: 360px; margin: auto;">

                                        <div class="card-content" style="text-align: center">     
                                        <p style="font-size: 30px">로그인</p>                             
                                            <div class="content" style="margin-top: 40px">
                                                <ul class="social_button">
                                                    <li>
                                                        <button class="img_naver" onclick="window.location.href='/oauth/naver'"></button>
                                                    </li>
                                                    <li>
                                                        <button class="img_google" onclick="window.location.href='/oauth/google'"></button>
                                                    </li>
                                                    <li>
                                                        <button class="img_naver" onclick="window.location.href='/oauth/naver'"></button>
                                                    </li>
                                                </ul>                                                
                                            </div>

                                        </div>

                                </div>
                                <button class="modal-close is-large" aria-label="close" onclick="close_modal()"></button>
                            </div>`
    $('body').append(tmp_html)
}

function close_modal() {
    $(".modal").removeClass("is-active");
    $(".modal").empty();
}


function logout() {

    $.removeCookie("mytoken");
    alert('로그아웃')
    window.location.href = '/'
}

//네이버로그인
function getnaverAccessToken() {
    naver.Auth.login({
        success: function (response) {
            "https://openapi.naver.com".request({
                url: '/v1/nid/me',
                success: function (response) {
                    accessToken = naver.Auth.getAccessToken();
                    naverLogin(accessToken);
                },
                fail: function (error) {
                    alert("네이버 인증에러!!")
                },
            })
        },
        fail: function (error) {
            alert("네이버 인증에러!!")
        },
    })
}

function naverLogin(accessToken) {
    $.ajax({
        type: "POST",
        url: `${gUrl}/naver-login`,
        data: JSON.stringify({access_token: accessToken}),
        success: function (response) {
            localStorage.setItem('token', response['token']);
            alert("로그인 되었습니다!!");
            // loginCheck();
        }
    })
}


