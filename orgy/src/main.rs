use std::io::{self, Read};

use pest::Parser;
use pest_derive;

#[derive(pest_derive::Parser)]
#[grammar = "playlist.pest"]
pub struct PlaylistParser;

#[derive(Debug)]
struct PlaylistItem<'a> {
    interpret: &'a str,
    title: &'a str,
}

fn parse_playlist(pair: pest::iterators::Pair<Rule>) -> Vec<PlaylistItem> {
    match pair.as_rule() {
        Rule::entries => pair.into_inner().flat_map(parse_playlist).collect(),
        Rule::entry => {
            let mut inner = pair.into_inner();
            vec!(PlaylistItem { interpret: inner.next().unwrap().as_str(),
                                title: inner.next().unwrap().as_str() })
        },
        Rule::playlist => parse_playlist(pair.into_inner().next().unwrap()),
        Rule::interprete | Rule::title | Rule::EOI | Rule::WHITESPACE => unreachable!(),
    }
}

fn strictly_alphabetically_ordered(playlist: Vec<PlaylistItem>) -> bool {
    playlist.iter().zip(&playlist[1..]).all(|x| x.0.interpret < x.1.interpret)
}

fn main() -> std::io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let pair = PlaylistParser::parse(Rule::playlist, &input).unwrap().next().unwrap();
    let playlist = parse_playlist(pair);
    match strictly_alphabetically_ordered(playlist) {
        true => Ok(()),
        false => Err(std::io::Error::from_raw_os_error(1))
    }
}
