<!DOCTYPE html>

<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>NIK INDONESIA</title>
    <style>
        body {
            font-family: sans-serif;
        }

        .panel {
            width: 400px;
        } 

        .input-group {
            position: relative;
        }

        .input {
            padding: 10px;
            background: white;
            border-radius: 2px;
            outline: none;
            color: #444444 !important;
            border: 1px solid #0da2ff !important;
            width: 327.14px;
        }

        .placeholder {
            position: absolute;
            top: 10px;
            left: 8px;
            font-size: 14px;
            padding: 0px 5px;
            color: #0da2ff !important;
            transition: 0.3s;
            pointer-events: none;
        }

        .input:focus+.placeholder,
        .input:not(:placeholder-shown)+.placeholder {
            top: -10px;
            background-color: white;
        }
    </style>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>

<body>
    <br><br><br><br><br>
    <center>
    <div class="panel panel-primary">
        <div class="panel-heading">Cek Nomor Induk Kependudukan</div>
        <div class="panel-body">
                <table class='table' style='width: 20px'>
                    <tr>
                        <td colspan="2">
                            <form action="." method="post">
                                <div class="input-group">
                                    <input type="number" class="input" placeholder=" " name="nik" maxlength="16" />
                                    <label class="placeholder">Masukan NIK</label>
                                </div>
                            </form>
                        </td>
                    </tr>
                    <?php
                    if (isset($_POST['nik'])) {
                        include 'functions.php';
                        $get_nik = $_POST['nik'];
                        $parsed = parseNik($get_nik);
                        if ($parsed->status == "false") {
                            echo "<tr>
                            <td colspan=2>
                            <div class='alert alert-danger'>
                            <strong>$parsed->message</strong>
                            </div>
                            </td>
                            </tr>";
                        } else {
                            echo "
                        <tr>
                            <td>Nomor Urut</td>
                            <td><input value='$parsed->urutan' disabled></td>
                        </tr>
                        <tr>
                        <td>Jenis Kelamin</td>
                            <td><input value='$parsed->jenis_kelamin' disabled></td>
                        </tr>
                        <tr>
                        <td>Tanggal Lahir</td>
                        <td><input value='$parsed->lahir' disabled></td>
                        </tr>
                        <tr>
                        <td>Kecamatan</td>
                        <td><input value='$parsed->kecamatan' disabled></td>
                        </tr>
                        <tr>
                        <td>Kodepos</td>
                        <td><input value='$parsed->kodepos' disabled></td>
                        </tr>
                        <tr>
                        <td>Kabupaten/Kota</td>
                        <td><input value='$parsed->kota' disabled></td>
                        </tr>
                        <tr>
                        <td>Provinsi</td>
                        <td><input value='$parsed->provinsi' disabled></td>
                        </tr>
                        </table>";
                        }
                    } else {
                        echo "</table>";
                    }
                    ?>
        </div>
    </div>
</body>

</html>
