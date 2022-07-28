$source_lang = $args[0]
$destination_lang = $args[1]
$path = $args[2]


Get-ChildItem -Path $path -Filter *.xml -Recurse -File| Sort-Object Length -Descending | ForEach-Object {
    $full_path_file = $_.FullName
    $full_path_file_new_xml_file = $full_path_file.replace($source_lang,$destination_lang)
    #write($full_path_file_new_xml_file)
    try{
        $sent ='Translate the file ' + $full_path_file + " ? [y or n]"
        $response = Read-Host $sent
        if( $response -eq "y"){
            New-Item -ItemType File -Path $full_path_file_new_xml_file -Force
            python translate_xml_file.py --file_path=$full_path_file --target_language="FRENCH" --module_api="DEEPL" --file_name_destination=$full_path_file_new_xml_file
        }else{
            $b = Test-Path $full_path_file_new_xml_file
            if($b){

            }else{
                New-Item -ItemType File -Path $full_path_file_new_xml_file -Force
                Copy-Item $full_path_file -Destination $full_path_file_new_xml_file
            }
        }
    }
    catch{

    }
}
