<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>正弦波アニメーション</title>
    <style>
        body { background: #f0f0f0; text-align: center; font-family: sans-serif; }
        canvas { background: white; margin-top: 20px; border: 1px solid #ccc; }
    </style>
</head>
<body>

<h2>正弦波が右に進むアニメーション</h2>
<p>位相を変えることで、波が右に進んでいるように見えます。</p>
<canvas id="canvas" width="800" height="300"></canvas>

<script>
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

let phase = 0;  // 位相（これが変化すると波が動く）

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.beginPath();
    ctx.lineWidth = 2;
    ctx.strokeStyle = "blue";

    for (let x = 0; x < canvas.width; x++) {
        // x を 0〜2π に変換
        let rad = (x / canvas.width) * 2 * Math.PI;

        // 正弦波（右に進む → rad - phase）
        let y = Math.sin(rad - phase);

        // キャンバス座標に変換
        let drawY = canvas.height / 2 - y * 100;

        if (x === 0) {
            ctx.moveTo(x, drawY);
        } else {
            ctx.lineTo(x, drawY);
        }
    }

    ctx.stroke();

    // 位相を少しずつ増やす → 波が右へ進む
    phase += 0.05;

    requestAnimationFrame(draw);
}

draw();
</script>

</body>
</html>
