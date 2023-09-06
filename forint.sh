if site=$(curl "https://www.wisselkoers.nl/hongaarse_forint"); then
        servers=$(echo "$site" | grep '<span class="euro-unit"' | grep -oE '[0-9]+,[0-9]+' | head -n 1)
        echo $servers
    fi