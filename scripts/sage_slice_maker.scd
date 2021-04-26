Server.killAll();

(
s.waitForBoot({
    b = Buffer.read(s, "/Users/james/Documents/Max 8/Packages/FluidCorpusManipulation/media/Tremblay-ASWINE-ScratchySynth-M.wav");
    s.sync;

    c = Buffer.new(s);

    FluidBufNoveltySlice.process(s, b, indices:c, action:{

        c.loadToFloatArray(action:{ | indices | ~indices = indices.as(Array) });

        s.sync;

        if(~indices.size > 0, {
            if(~indices[0] != 0, {
                ~indices = ~indices.insert(0, 0)
            })
        });

        ~indices.do({ | index, i |
            var color, next_index;
            if(i < (~indices.size - 1), {
                next_index = ~indices[i + 1]
            }, {
                next_index = b.numFrames
            });
            color = Color.rand(0.0, 1.0).hexString;
            ~indices[i] = [index, next_index, color]
        });

        ~rand_indices = ~indices.scramble;

        ~final_array  = Array.newClear;

        ~rand_samples = Array.newClear;

        ~rand_indices.do({ | entry |
            var index = entry[0].asInteger;
            var next_index = entry[1].asInteger;
            var color = entry[2];
            b.loadToFloatArray(index, next_index - index, { | samples |
                ~rand_samples = ~rand_samples.add(samples);
            });

            ~final_array = ~final_array.add((
                start: index,
                end: next_index,
                color: color
            ));
        });

        s.sync;

        ~rand_samples = ~rand_samples.flatten;

        d = Buffer.loadCollection(s, ~rand_samples, b.numChannels);

        s.sync;

        d.play;

        ~final_array.postln;

    });
});
)