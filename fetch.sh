if [ ! -d tmp ]; then
        mkdir tmp
fi

for url in $(cat ZINC-downloader-3D-sdf.gz.curl); do
        output=$(basename "$url")
        if [ ! -f "$output" ]; then
                (cd tmp && wget -c "$url" && mv "$output" ..)
        fi
done

echo DONE
