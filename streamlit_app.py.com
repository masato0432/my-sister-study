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

let phase = 0;

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.beginPath();
    ctx.lineWidth = 2;
    ctx.strokeStyle = "blue";

    for (let x = 0; x < canvas.width; x++) {
        const rad = (x / canvas.width) * 2 * Math.PI;
        const y = Math.sin(rad - phase);
        const drawY = canvas.height / 2 - y * 100;

        if (x === 0) ctx.moveTo(x, drawY);
        else ctx.lineTo(x, drawY);
    }

    ctx.stroke();
    phase += 0.05;

    requestAnimationFrame(draw);
}

draw();
</script>

</body>
</html>
