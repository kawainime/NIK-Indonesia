<?php
function parseNik($nik) {
    include 'database.php';
    $panjangNIK = strlen($nik);
    if ($panjangNIK > 16 || $panjangNIK < 16) {
        $result = new stdClass();
        $result->status = "false";
        $result->message = "NIK HARUS 16 DIGIT, TERDETEKSI $panjangNIK DIGIT!";
        return $result;
    } else {
        $prov_index = "$nik[0]$nik[1]"; # 2 Digit Provinsi
        $kota_index = "$nik[2]$nik[3]"; # 2 Digit Kabupaten/Kota
        $kec_index = "$nik[4]$nik[5]"; # 2 Digit Kecamatan
        $jenis_kelamin = (int) "$nik[6]$nik[7]" > 31 ? "PEREMPUAN" : "LAKI-LAKI"; # Jenis kelamin apabila melebihi tanggal dari bulan maka laki2
        $tgl = $jenis_kelamin == "PEREMPUAN" ? ((int) "$nik[6]$nik[7]" - 40) : (int) "$nik[6]$nik[7]" ;
        $lahir = "$tgl$nik[8]$nik[9]$nik[10]$nik[11]"; # 6 Digit tanggal lahir / hhbbtt
        $urutan = (int) "$nik[12]$nik[13]$nik[14]$nik[15]"; # 4 Digit nomor urut

        $prov = $provinsi[$prov_index];
        $kota = $kabkot["$prov_index$kota_index"];
        $kec = $kecamatan["$prov_index$kota_index$kec_index"];
        $tgl_lahir = DateTime::createFromFormat('dmy', $lahir)->format('d-m-Y');

        $result = new stdClass();
        $result->status = "true";
        $result->urutan = $urutan;
        $result->jenis_kelamin = $jenis_kelamin;
        $result->provinsi = $prov;
        $result->kota = $kota;
        $result->kecamatan = explode(" | ", $kec)[0];
        $result->kodepos = explode(" | ", $kec)[1];
        $result->lahir = $tgl_lahir;

        return $result;
    }
}
?>
