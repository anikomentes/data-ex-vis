
curl -s "https://ourworldindata.org/grapher/life-expectancy.csv?v=1&csvType=full&useColumnShortNames=true"
curl -s "https://ourworldindata.org/grapher/life-expectancy.csv?v=1&useColumnShortNames=false" |head
curl -s "https://ourworldindata.org/grapher/life-expectancy.metadata.json" | json_pp
